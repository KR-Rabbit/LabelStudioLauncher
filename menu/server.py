import pathlib

from PySide6.QtCore import QDateTime, Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog

import utils
from ui.Server_UI import Ui_Server
from utils import generate_json_file
from utils.global_manager import manager
from utils.porcess import Process
from utils.thread import Executor

current_config = manager.get_()


class Server(QMainWindow):

    def __init__(self, installed: bool, latest_check: int, data_root: str, data_path: str):
        super().__init__()
        self.ui = Ui_Server()
        self.ui.setupUi(self)
        self._latest_check = latest_check
        self._installed = installed
        self._data_root = pathlib.Path(data_root) if data_root else ""
        self._data_path = pathlib.Path(data_path) if data_path else ""

        self._check_process = None
        self._install_process = None
        self._check_state = None
        self._executor = None
        self.init_settings()

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.show()

    def init_settings(self):
        self._data_root = self._data_root if self._data_root and self._data_root.exists() else ""
        self._data_path = self._data_path if self._data_path and self._data_path.exists() else self._data_root
        self.ui.lineEdit_data_root.setText(str(self._data_root) if self._data_root else "")
        self.ui.lineEdit_data.setText(str(self._data_path) if self._data_path else "")
        current_timestamp = QDateTime.currentDateTime().toSecsSinceEpoch()
        self.ui.pushButton_check.setEnabled(current_timestamp - self._latest_check > 7 * 24 * 60 * 60)
        self.ui.pushButton_install.setEnabled(not self._installed)
        self.ui.pushButton_generate.setEnabled(bool(self._data_root and self._data_path))
        self.ui.pushButton_data.setEnabled(
            bool(self._data_root and self._data_path and self._data_path.is_relative_to(self._data_root)))

    def check_studio(self):
        global current_config
        python_path = utils.get_python_exe_path(current_config.get("conda"))
        if not python_path or not python_path.exists():
            self.statusBar().showMessage("Python解释器路径错误，检查失败", 6000)
            return
        self.ui.pushButton_check.setEnabled(False)
        self._check_process = Process(python_path.__str__(), "-m pip show label_studio".split())
        self._check_process.readyRead.connect(lambda: self.get_check_state(self._check_process.info))
        self._check_process.finished.connect(self.check_studio_finished)
        self._check_process.start()

    def get_check_state(self, info):
        self._check_state = info
        self.statusBar().showMessage(info, 1000)

    def check_studio_finished(self):
        self.ui.pushButton_check.setEnabled(True)
        if self._check_state is None:
            replay = QMessageBox.information(self, "Tip", "Label Studio 未安装.\r\n是否安装？",
                                             QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            if replay == QMessageBox.StandardButton.Ok:
                self.install_studio()
            self.ui.pushButton_install.setEnabled(True)
            self._installed = False
        else:
            self._installed = True
            self._latest_check = QDateTime.currentDateTime().toSecsSinceEpoch()
            self.statusBar().showMessage("Label Studio 已安装", 6000)
            self.ui.pushButton_check.setEnabled(False)
            self.ui.pushButton_install.setEnabled(False)

    def install_studio(self):
        global current_config
        python_path = utils.get_python_exe_path(current_config.get("conda"))
        if not python_path or not python_path.exists():
            self.statusBar().showMessage("Python解释器路径错误，请检查配置", 6000)
            return
        replay = QMessageBox.question(self, "Tip",
                                      f"确定将label-studio安装到{current_config.get('conda').get('env_name')}虚拟环境中?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.Yes)
        if replay == QMessageBox.StandardButton.No:
            return
        self.ui.pushButton_install.setEnabled(False)
        self._install_process = Process(python_path.__str__(), "-m pip install label-studio".split())
        self._install_process.finished.connect(self.install_studio_finished)
        self._install_process.readyRead.connect(lambda: self.statusBar().showMessage(self._install_process.info), 5000)
        self._install_process.start()

    def install_studio_finished(self):
        self._installed = True
        self._latest_check = QDateTime.currentDateTime().toSecsSinceEpoch()
        self.ui.pushButton_install.setEnabled(False)
        self.ui.pushButton_check.setEnabled(False)
        QMessageBox.information(self, "Tip", "Label Studio 安装完成.", QMessageBox.StandardButton.Ok)

    def select_root(self):
        data_root = QFileDialog.getExistingDirectory(self, "选择数据根目录",
                                                     self._data_root.__str__() if self._data_root else ".")
        if data_root != "":
            self._data_root = pathlib.Path(data_root)
            self.ui.lineEdit_data_root.setText(data_root)
            self.ui.pushButton_data.setEnabled(True)
            if not self.check_data_path():
                self._data_path = ""
                self.ui.lineEdit_data.clear()
                self.ui.pushButton_generate.setEnabled(False)

    def select_data_path(self):
        data_path = QFileDialog.getExistingDirectory(self, "选择数据目录",
                                                     self._data_path.__str__() if self._data_path else self._data_root.
                                                     __str__() if self._data_root else ".")
        if data_path != "" and pathlib.Path(data_path).is_relative_to(self._data_root):
            self._data_path = pathlib.Path(data_path)
            self.ui.lineEdit_data.setText(data_path)
            self.ui.pushButton_generate.setEnabled(True)
        else:
            self.statusBar().showMessage("请选择正确的数据根目录的子目录", 4000)

    def generate_json(self):

        if self._data_root == "" or not pathlib.Path(self._data_root).exists():
            QMessageBox.information(self, "Tip", "请选择合法的数据根目录", QMessageBox.StandardButton.Ok)
            return
        if self._data_path == "" or not pathlib.Path(self._data_path).exists() and not pathlib.Path(
                self._data_path).is_relative_to(self._data_root):
            self.statusBar().showMessage("请选择合法的数据目录", 4000)
            return
        self.ui.pushButton_generate.setEnabled(False)
        self._executor = Executor(generate_json_file, self._data_root, self._data_path)
        self._executor.finished.connect(self.generate_json_finished)
        self._executor.start()

    def generate_json_finished(self):
        self.statusBar().showMessage("生成json文件完成", 4000)
        self.ui.pushButton_generate.setEnabled(True)

    def check_data_path(self):
        if self._data_path == "" or not pathlib.Path(self._data_path).is_relative_to(self._data_root):
            return False
        return True

    def save_setting(self):
        global current_config
        current_config.get("server").update(
            latest_check=self._latest_check,
            installed=self._installed,
            data_root=self._data_root.__str__() if self._data_root else "",
            data_path=self._data_path.__str__() if self._data_path else "",
        )
        manager.save_(current_config)

    def closeEvent(self, event) -> None:
        self.save_setting()
        event.accept()
