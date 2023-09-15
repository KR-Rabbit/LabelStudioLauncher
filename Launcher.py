import pathlib
import sys

from PySide6.QtCore import QProcess
from PySide6.QtGui import Qt, QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QSystemTrayIcon, QMenu

import utils
from menu.common import Common
from menu.conda import Conda
from menu.help import Help
from menu.server import Server
from ui import ico_rc
from ui.Launcher_UI import Ui_LabelStudio
from utils.global_manager import manager
from utils.porcess import Process

current_config = manager.get_()
name = ico_rc.qt_resource_name


class Launcher(QMainWindow):
    from_system_tray = False

    def __init__(self):
        super().__init__()

        self.ui = Ui_LabelStudio()
        self.ui.setupUi(self)
        self.conda_ui = None
        self.server_ui = None
        self.common_ui = None
        self.help_ui = None

        self.check_processor = None
        self.http_processor = None
        self.studio_processor = None

        self.close_type = "minimize"
        self.second_confirm = False

        self.system_tray = QSystemTrayIcon(QIcon(u":/main/launcher.ico"), self)
        self.system_tray.activated.connect(self.tray_activated)
        self.menu = QMenu(self)
        self.action_show = QAction("隐藏界面", self)
        self.action_close = QAction("退出", self)
        self.action_show.triggered.connect(self.show_)
        self.action_close.triggered.connect(self.close_)
        self.menu.addAction(self.action_show)
        self.menu.addAction(self.action_close)
        self.system_tray.setContextMenu(self.menu)
        self.system_tray.setToolTip("Label Studio")
        self.system_tray.show()
        self.init_main_setting()
        self.show()

    def init_main_setting(self):
        global current_config
        main_config = current_config.get("main")
        self.second_confirm = main_config.get("second_confirm")
        self.close_type = main_config.get("close_type")

    def set_conda(self):
        global current_config
        if self.conda_ui is None:
            self.conda_ui = Conda(**current_config.get("conda"))
        self.conda_ui.show()

    def set_server(self):
        global current_config
        conda_config = current_config.get("conda")
        conda_root = conda_config.get("conda_root") if conda_config.get("conda_root") else ""
        env_name = conda_config.get("env_name") if conda_config.get("env_name") else ""
        python_path_config = pathlib.Path(conda_root, "python.exe") if env_name == "base" \
            else pathlib.Path(conda_root, "envs", env_name, "python.exe")
        if not python_path_config.exists():
            QMessageBox.information(self, "Tip", "清先进行Conda设置初始化", QMessageBox.StandardButton.Yes)
            return
        if self.server_ui is None:
            self.server_ui = Server(**current_config.get("server"))
        self.server_ui.show()

    def set_common(self):
        global current_config
        main_config = current_config.get("main")
        self.second_confirm = main_config.get("second_confirm")
        self.close_type = main_config.get("close_type")
        if not self.common_ui:
            self.common_ui = Common()
        self.common_ui.show()

    def abort(self):
        if not self.help_ui:
            self.help_ui = Help()
        self.help_ui.show()

    def start(self):
        self.ui.pushButton_start.setEnabled(False)
        global current_config
        python_path = utils.get_python_exe_path(current_config.get("conda"))
        if not python_path:
            QMessageBox.information(self, "Tip", "请先进行Conda设置初始化", QMessageBox.StandardButton.Yes)
            self.ui.pushButton_start.setEnabled(True)
            return
        self.check_processor = QProcess()
        self.check_processor.start(python_path.__str__(), "-m pip show label_studio".split())
        self.check_processor.finished.connect(self.check_finished)

    def check_finished(self):
        global current_config
        if self.check_processor.exitCode() != 0:
            QMessageBox.information(self, "Tip", "请先安装label_studio", QMessageBox.StandardButton.Yes)
            self.ui.pushButton_start.setEnabled(True)
            return
        else:
            data_root = utils.get_data_root(current_config.get("server"))
            if not data_root:
                self.ui.pushButton_start.setEnabled(True)
                return
            self.studio_processor = Process(utils.get_python_exe_path(current_config.get("conda")).__str__(),
                                            "-m label_studio.server".split())
            self.studio_processor.start()
            self.studio_processor.readyRead.connect(
                lambda: self.ui.textBrowser_studio.append(self.studio_processor.info))
            self.http_processor = Process(utils.get_python_exe_path(current_config.get("conda")).__str__(),
                                          f"-m http.server -d {data_root}".split())
            self.http_processor.start()
            self.http_processor.readyRead.connect(
                lambda: self.ui.textBrowser_http.append(self.http_processor.info))
            self.ui.pushButton_start.setEnabled(False)
            self.ui.pushButton_start.setText("服务运行中...")
        self.check_processor.close()
        self.check_processor = None

    def close_processor(self):
        if self.check_processor:
            self.check_processor.close()
        if self.studio_processor:
            self.studio_processor.close()
        if self.http_processor:
            self.http_processor.close()

    def close_window(self):
        global current_config
        manager.save_(current_config)
        self.close_processor()

    def show_(self):
        if self.isMinimized() or not self.isVisible():
            # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
            self.show_normal()
        else:
            self.hide_from_bar()

    def close_(self):
        self.from_system_tray = True
        self.close()
        QApplication.quit()

    def show_normal(self):
        self.showNormal()
        self.activateWindow()
        # self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowStaysOnTopHint)
        self.action_show.setText("隐藏界面")
        self.show()

    def hide_from_bar(self):
        self.showMinimized()
        self.setWindowFlags(Qt.WindowType.SplashScreen)
        self.action_show.setText("显示界面")
        self.show()

    def closeEvent(self, event) -> None:
        if self.from_system_tray:
            self.close_window()
            event.accept()
            return
        global current_config
        main_config = current_config.get("main")
        self.close_type = main_config.get("close_type", "minimize")
        self.second_confirm = main_config.get("second_confirm", False)
        if self.close_type == "minimize":
            self.hide_from_bar()
            event.ignore()

        elif self.second_confirm:
            replay = QMessageBox.question(self, "提示", "是否退出程序？",
                                          QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                          QMessageBox.StandardButton.Yes)
            if replay == QMessageBox.StandardButton.Yes:
                self.close_window()
                event.accept()
            else:
                event.ignore()
        else:
            self.close_window()
            event.accept()

    def tray_activated(self, reason):  # 托盘双击
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            if self.isMinimized():
                print("close")
                self.show_normal()
            else:
                self.hide_from_bar()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = Launcher()
    sys.exit(app.exec())
