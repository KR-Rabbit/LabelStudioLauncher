import pathlib

from PySide6.QtCore import QDateTime, Qt, QProcess
from PySide6.QtGui import QRegularExpressionValidator, QIntValidator, QGuiApplication
from PySide6.QtWidgets import QMessageBox, QFileDialog

import utils
from menu import Base
from ui.Server_UI import Ui_Server
from utils.global_manager import manager
from utils.thread import Executor

current_config = manager.get_()


# noinspection PyUnresolvedReferences
class Server(Base):  # 服务设置

    def __init__(self, installed: bool, latest_check: int, data_root: str, data_path: str,
                 http_address=None, recursive=False):
        super().__init__()
        if http_address is None:
            http_address = {"ip": "localhost", "port": 8000}
        self.ui = Ui_Server()
        self.ui.setupUi(self)
        self._latest_check = latest_check  # 最近一次检验时间
        self._installed = installed  # 是否安装Label Studio
        self._data_root = pathlib.Path(data_root) if data_root else ""
        self._data_path = pathlib.Path(data_path) if data_path else ""
        self._ip = http_address.get("ip", "localhost")
        self._port = http_address.get("port", 8000)
        self._check_process = None  # Label Studio检查线程
        self._install_process = None  # 安装Label Studio线程
        self._check_state = None  # install_process 在未检测到Label Studio时，在读取通道准备完成时，程序已经执行完毕，不会返回有效值
        self._executor = None  # 生成json属于耗时的IO, 开辟新的线程执行json生成
        self._recursive = recursive  # 是否递归检索子目录中的图像

        self.ui.lineEdit_ip.setValidator(QRegularExpressionValidator(utils.IP_REG))
        self.ui.lineEdit_port.setValidator(QIntValidator(0, 65535))
        self.init_settings()

        # 输入框输入约束

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.show()

    def init_settings(self):
        self._data_root = self._data_root if self._data_root and self._data_root.exists() else ""
        self._data_path = self._data_path if self._data_path and self._data_path.exists() else self._data_root
        self.ui.lineEdit_data_root.setText(str(self._data_root) if self._data_root else "")
        self.ui.lineEdit_data.setText(str(self._data_path) if self._data_path else "")
        self.ui.checkBox_recursive.setChecked(self._recursive)
        self.ui.lineEdit_ip.setText(self._ip)
        self.ui.lineEdit_port.setText(str(self._port))
        current_timestamp = QDateTime.currentDateTime().toSecsSinceEpoch()
        self.ui.pushButton_check.setEnabled(current_timestamp - self._latest_check > 7 * 24 * 60 * 60)  # 7天内不检查安装状态
        self.ui.pushButton_install.setEnabled(not self._installed)
        self.ui.pushButton_generate.setEnabled(bool(self._data_root and self._data_path))  # 数据路径合法时可以生成json
        self.ui.pushButton_data.setEnabled(
            bool(self._data_root and self._data_path and self._data_path.is_relative_to(self._data_root)))

    def check_studio(self):
        global current_config
        python_path = utils.get_python_exe_path(current_config.get("conda"))
        if not python_path or not python_path.exists():
            self.statusBar().showMessage("Python解释器路径错误，检查失败", 6000)
            return
        self.ui.pushButton_check.setEnabled(False)
        self._check_process = QProcess()
        self._check_process.setProgram(python_path.__str__())
        self._check_process.setArguments("-m pip show label_studio".split())
        self._check_process.readyReadStandardOutput.connect(self.read_process_info)
        self._check_process.finished.connect(self.check_studio_finished)
        self._check_process.start()

    def read_process_info(self):
        info = self.sender().readAllStandardOutput().data().strip().decode()
        self._check_state = info
        self.statusBar().showMessage(info, 6000)

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
        self._install_process = QProcess()
        self._install_process.setProgram(python_path.__str__())
        self._install_process.setArguments("-m pip install label-studio".split())
        self._install_process.readyRead.connect(self.read_process_info)
        self._install_process.finished.connect(self.install_studio_finished)
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
        self.ui.pushButton_generate.setText("正在生成...")
        ip = self.ui.lineEdit_ip.text()
        port = self.ui.lineEdit_port.text()
        recursive = self.ui.checkBox_recursive.isChecked()
        self._executor = Executor(self._data_root, self._data_path, ip=ip, port=port, recursive=recursive)
        self._executor.finished.connect(self.generate_json_finished)
        self._executor.start()

    def generate_json_finished(self):
        self.statusBar().showMessage(f"JSON文件生成完成，保存在{self.sender().result}，请在剪贴板查看路径", 6000)
        # 路径复制到剪切板
        QGuiApplication.clipboard().setText(self.sender().result)
        self._executor = None
        self.ui.pushButton_generate.setEnabled(True)
        self.ui.pushButton_generate.setText("生成JSON文件")

    def check_data_path(self):
        if self._data_path == "" or not pathlib.Path(self._data_path).is_relative_to(self._data_root):
            return False
        return True

    def change_recursive(self):
        self._recursive = self.sender().isChecked()

    def save_setting(self):
        global current_config
        self._ip = utils.ip_check(self.ui.lineEdit_ip.text(), to_json=False)
        self._port = utils.port_check(self.ui.lineEdit_port.text(), rtype=int)
        current_config.get("server").update(
            latest_check=self._latest_check,
            installed=self._installed,
            data_root=self._data_root.__str__() if self._data_root else "",
            data_path=self._data_path.__str__() if self._data_path else "",
            http_address=dict(ip=self._ip, port=self._port),
            recursive=self._recursive
        )
        manager.save_(current_config)

    def closeEvent(self, event) -> None:
        self.save_setting()
        if self._executor:
            self._executor.stop = True
            while not self._executor.stopped:  # 等待循环结束
                pass
        super().closeEvent(event)
