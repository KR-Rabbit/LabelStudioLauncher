import pathlib
import sys
import time

from PySide6.QtCore import QProcess, Slot
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
from utils.porcess.http import CORS_HTTPServer

current_config = manager.get_()
name = ico_rc.qt_resource_name


class Launcher(QMainWindow):
    from_system_tray = False

    def __init__(self):
        super().__init__()

        self.close_from_sub = False
        self.tray_flag = False  # 托盘标志位,还是为了解决双触发问题
        self.ui = Ui_LabelStudio()
        self.ui.setupUi(self)

        self.conda_ui = None  # anaconda配置页面
        self.server_ui = None  # 服务与数据配置页面
        self.common_ui = None  # 常规设置页面
        self.help_ui = None  # 帮助页面

        self.check_processor = None  # 检查label_studio是否安装
        self.http_server = None  # http服务进程
        self.studio_processor = None  # label_studio服务进程

        self.close_type = "minimize"  # 关闭方式,默认最小化
        self.second_confirm = False  # 是否二次确认,默认不二次确认

        self.system_tray = QSystemTrayIcon(QIcon(u":/main/launcher.ico"), self)  # 系统托盘
        self.system_tray.activated.connect(self.tray_activated)  # 托盘双击事件
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
        self.init_window_flags = self.windowFlags()

    def init_main_setting(self):
        """
        初始化主要设置
        """
        global current_config
        main_config = current_config.get("main")
        self.second_confirm = main_config.get("second_confirm")
        self.close_type = main_config.get("close_type")

    def set_conda(self):
        """
        设置conda
        """
        global current_config
        if self.conda_ui is None:
            self.conda_ui = Conda(**current_config.get("conda"))
        self.conda_ui.show()
        self.conda_ui.closed.connect(self.sub_window_closed)

    def set_server(self):
        """
        设置服务与数据
        :return:
        """
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
        self.server_ui.closed.connect(self.sub_window_closed)

    def set_common(self):
        """
        常规设置
        """
        global current_config
        main_config = current_config.get("main")
        self.second_confirm = main_config.get("second_confirm")
        self.close_type = main_config.get("close_type")
        if not self.common_ui:
            self.common_ui = Common()
        self.common_ui.show()
        self.common_ui.closed.connect(self.sub_window_closed)

    def abort(self):
        """
        关于
        """
        if not self.help_ui:
            self.help_ui = Help()
        self.help_ui.show()
        self.help_ui.closed.connect(self.sub_window_closed)

    def start(self):
        """
        启动服务
        :return:
        """
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
        """
        检查label_studio是否安装完成后触发的事件
        :return:
        """
        global current_config
        if self.check_processor.exitCode() != 0:
            QMessageBox.information(self, "Tip", "请先安装label_studio", QMessageBox.StandardButton.Yes)
            self.ui.pushButton_start.setEnabled(True)
            return
        else:
            data_root = utils.get_data_root(current_config.get("server"))
            if not data_root:
                self.ui.pushButton_start.setEnabled(True)
                QMessageBox.information(self, "Tip", "请先设置数据目录", QMessageBox.StandardButton.Yes)
                return
            self.studio_processor = Process(utils.get_python_exe_path(current_config.get("conda")).__str__(),
                                            "-m label_studio.server".split())
            self.studio_processor.start()
            self.studio_processor.readyRead.connect(
                lambda: self.ui.textBrowser_studio.append(self.studio_processor.info))
            self.http_server = CORS_HTTPServer(directory=data_root)
            self.http_server.start()
            self.ui.pushButton_start.setEnabled(False)
            self.ui.pushButton_start.setText("服务运行中...")
        self.check_processor.close()
        self.check_processor = None

    def close_processor(self):
        if self.check_processor:
            self.check_processor.close()
        if self.studio_processor:
            self.studio_processor.close()
        if self.http_server:
            self.http_server.stop()

    def close_window(self):
        global current_config
        manager.save_(current_config)
        self.close_processor()

    def show_(self):
        if self.isMinimized() or not self.isVisible():
            self.show_normal()
        else:
            self.hide_from_bar()

    def close_(self):
        self.from_system_tray = True
        self.close()
        QApplication.quit()

    def show_normal(self):
        self.showNormal()
        # self.activateWindow()
        # self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlags(self.init_window_flags)
        self.action_show.setText("隐藏界面")
        self.show()

    def hide_from_bar(self):
        """
        从任务栏隐藏,并显示在托盘
        """
        self.tray_flag = True
        self.showMinimized()
        self.setWindowFlags(Qt.WindowType.SplashScreen)
        self.action_show.setText("显示界面")
        self.show()

    def closeEvent(self, event) -> None:
        # 时间格式化
        if self.from_system_tray:
            self.close_window()
            event.accept()
            return
        if self.tray_flag and self.close_from_sub:  # 托盘触发以后才会有双触发问题
            self.close_from_sub = False
            event.ignore()
            return
        self.close_main(event)

    def close_main(self, event):
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
                self.show_normal()
            else:
                self.hide_from_bar()

    @Slot(str)
    def sub_window_closed(self, window_name):
        if window_name == self.conda_ui.__class__.__name__:
            self.conda_ui = None
        elif window_name == self.server_ui.__class__.__name__:
            self.server_ui = None
        elif window_name == self.common_ui.__class__.__name__:
            self.common_ui = None
        else:
            self.help_ui = None
        self.close_from_sub = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = Launcher()
    sys.exit(app.exec())
