import pathlib

from PySide6.QtCore import Qt, QProcess
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QFileDialog, QButtonGroup, QMessageBox

import utils
from menu import Base
from ui.Conda_UI import Ui_Conda
from utils import format_conda_path, is_conda_path
from utils.global_manager import manager

current_config = manager.get_()


class Conda(Base):  # Conda设置

    def __init__(self, conda_root, conda_exec_path, env_name):

        super().__init__()
        self.create_process = None
        self.ui = Ui_Conda()
        self.ui.setupUi(self)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.ui.radioButton_current)
        self.button_group.addButton(self.ui.radioButton_new)
        self.button_group.buttonClicked.connect(self.adjust_widgets)
        self._conda_root = pathlib.Path(conda_root)  # conda根目录
        self._conda_exec_path = pathlib.Path(conda_exec_path)  # conda 可执行文件路径
        self._env_name = env_name

        self.init_settings()  # 初始化设置
        self.current_status()  # 设置当前控件状态
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)  # 窗口置顶
        self.ui.lineEdit_env_name.setValidator(QRegularExpressionValidator("^[a-zA-Z0-9_-]+$"))  # 设置虚拟环境名的正则表达式
        self.show()

    def init_settings(self):  # 初始化设置
        if not utils.is_conda_root(self._conda_root):  # 判断conda的可执行文件或者bat脚本路径是否存在
            self._conda_root = format_conda_path(self._conda_root)  # 如果不存在，从系统环境变量中获取
        self._conda_exec_path = pathlib.Path(self._conda_exec_path) if is_conda_path(
            self._conda_exec_path) else pathlib.Path(self._conda_root,
                                                     "_conda.exe") if self._conda_root else None  # conda可执行文件路径
        self.ui.lineEdit_conda.setText(
            self._conda_exec_path.__str__() if self._conda_exec_path else "")  # 在界面上显示conda可执行文件路径
        self.set_current()  # 设置current_radio_button相关界面

    def set_current(self):
        # 设置current_radio_button相关界面
        envs = self.get_envs()  # 获取所有的虚拟环境列表
        for env in envs:
            self.ui.comboBox_envs.addItem(env)  # 在界面上显示虚拟环境列表
        if self._env_name in envs:
            self.ui.comboBox_envs.setCurrentIndex(envs.index(self._env_name))  # 设置选中的虚拟环境

    def select_conda(self):  # 选择conda可执行文件
        if not is_conda_path(self._conda_root):  # 判断conda的可执行文件或者bat脚本路径是否存在
            self._conda_root = format_conda_path(self._conda_root)
        filename, _ = QFileDialog.getOpenFileName(self, "Select Conda",
                                                  self._conda_root.__str__() if self._conda_root else ".",
                                                  "Conda (_conda.exe conda.bat conda.exe)")
        if not filename:
            return
        self.check_conda(filename)

    def create_env(self):  # 创建虚拟环境
        env_name = self.ui.lineEdit_env_name.text()
        if env_name == "":
            QMessageBox.information(self, "Tip", "请输入虚拟环境名", QMessageBox.StandardButton.Ok)
            return
        if env_name in self.get_envs():
            QMessageBox.information(self, "Tip", "虚拟环境已存在", QMessageBox.StandardButton.Ok)
            return
        version = self.ui.comboBox_version.currentText()
        cmd = f"create -n {env_name} python={version} --yes"
        conda_exe = pathlib.Path(self._conda_root, "Scripts", "conda.exe").as_posix()

        self.create_process = QProcess(self)
        self.create_process.setProgram(conda_exe)
        self.create_process.setArguments(cmd.split())
        self.create_process.setProcessChannelMode(QProcess.MergedChannels)
        self.create_process.readyReadStandardOutput.connect(self.create_process_output)
        self.create_process.start()
        self.ui.create_btn.setEnabled(False)
        self.ui.textBrowser.show()
        self.create_process.finished.connect(lambda: self.ui.create_btn.setEnabled(True))

    def create_process_output(self):
        self.ui.textBrowser.append(self.create_process.readAllStandardOutput().data().decode())

    def create_process_finished(self):
        self.ui.create_btn.setEnabled(True)
        self.create_process.close()
        self.create_process = None
        self.set_current()  # 更新虚拟环境列表
        self.ui.textBrowser.clear()
        self.ui.textBrowser.hide()

    def update_env_name(self):  # 更新虚拟环境名
        self._env_name = self.ui.comboBox_envs.currentText()

    def get_envs(self):  # 获取虚拟环境列表
        envs = [] if not "base" else ["base"]
        self.ui.comboBox_envs.clear()
        for file in self._conda_root.joinpath("envs").glob('*[!.]*'):  # *[!.]*匹配除了隐藏文件以外的所有文件
            if file.is_dir():
                envs.append(file.name)
        return envs

    def check_conda(self, filename):
        exec_path = ""
        if filename != "" and is_conda_path(filename):
            p = pathlib.Path(filename)
            if p.suffix == ".bat":
                self._conda_root = p.parent.parent  # conda根目录是bat的二级父目录
                exec_path = p.__str__()
            elif p.suffix == ".exe":
                self._conda_root = p.parent if p.name.startswith(
                    "_") else p.parent.parent  # conda根目录是_conda.exe的父目录,conda.exe的父父目录
                exec_path = p.__str__()
            for env in self.get_envs():
                self.ui.comboBox_envs.addItem(env)
        self.ui.lineEdit_conda.setText(exec_path)

    def adjust_widgets(self, btn):
        if btn == self.ui.radioButton_current:
            self.current_status()
        else:
            self.new_status()

    def current_status(self):
        self.ui.comboBox_envs.show()
        self.set_current()
        self.ui.lineEdit_env_name.hide()
        self.ui.comboBox_version.hide()
        self.ui.label_version_tip.hide()
        self.ui.create_btn.hide()
        self.ui.textBrowser.hide()

    def new_status(self):
        self.ui.comboBox_envs.hide()
        self.ui.lineEdit_env_name.show()
        self.ui.comboBox_version.show()
        self.ui.label_version_tip.show()
        self.ui.create_btn.show()

    def save_setting(self):
        global current_config
        current_config.get("conda").update(
            conda_root=self._conda_root.__str__(),
            conda_exec_path=self._conda_exec_path.__str__(),
            env_name=str(self._env_name)
        )
        manager.save_(current_config)

    def closeEvent(self, event) -> None:
        self.save_setting()
        super().closeEvent(event)
