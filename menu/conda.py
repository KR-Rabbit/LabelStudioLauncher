import pathlib

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QButtonGroup

import utils
from menu import Base
from ui.Conda_UI import Ui_Conda
from utils import format_conda_path, is_conda_path
from utils.global_manager import manager

current_config = manager.get_()


class Conda(Base):  # Conda设置

    def __init__(self, conda_root, conda_exec_path, env_name):

        super().__init__()
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
        self.show()

    def init_settings(self):  # 初始化设置
        if not utils.is_conda_root(self._conda_root):  # 判断conda的可执行文件或者bat脚本路径是否存在
            self._conda_root = format_conda_path(self._conda_root)  # 如果不存在，从系统环境变量中获取
        self._conda_exec_path = pathlib.Path(self._conda_exec_path) if is_conda_path(
            self._conda_exec_path) else pathlib.Path(self._conda_root,
                                                     "_conda.exe") if self._conda_root else None  # conda可执行文件路径
        self.ui.lineEdit_conda.setText(
            self._conda_exec_path.__str__() if self._conda_exec_path else "")  # 在界面上显示conda可执行文件路径
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
                                                  "Conda (_conda.exe conda.bat)")
        self.check_conda(filename)

    def update_env_name(self):  # 更新虚拟环境名
        self._env_name = self.ui.comboBox_envs.currentText()

    def get_envs(self):  # 获取虚拟环境列表
        envs = [] if not "base" else ["base"]
        self.ui.comboBox_envs.clear()
        for file in self._conda_root.joinpath("envs").glob('*[!.]*'):
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
                self._conda_root = p.parent  # conda根目录是exe的父目录
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
        self.ui.lineEdit_env_name.hide()
        self.ui.comboBox_version.hide()
        self.ui.label_version_tip.hide()

    def new_status(self):
        self.ui.comboBox_envs.hide()
        self.ui.lineEdit_env_name.show()
        self.ui.comboBox_version.show()
        self.ui.label_version_tip.show()

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
