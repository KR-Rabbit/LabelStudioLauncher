import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QButtonGroup, QApplication

from menu import Base
from ui.Common_UI import Ui_Common
from utils.global_manager import manager

current_config = manager.get_()


class Common(Base):  # 通用设置
    def __init__(self):
        super().__init__()
        self.ui = Ui_Common()
        self.ui.setupUi(self)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.ui.radioButton_close)
        self.button_group.addButton(self.ui.radioButton_min)
        self.button_group.buttonClicked.connect(self.on_radio_select)
        self.init_setting()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.show()

    def init_setting(self):  # 初始化设置
        global current_config
        main_config = current_config.get("main")
        close_type = main_config.get("close_type")
        if close_type == "close":
            self.ui.radioButton_close.setChecked(True)
        else:
            self.ui.radioButton_min.setChecked(True)
        self.ui.checkBox.setChecked(main_config.get("second_confirm"))

    def on_radio_select(self, radio):  # 选择关闭方式
        global current_config
        close_type = "close" if radio == self.ui.radioButton_close else "minimize"
        current_config.get("main").update(
            close_type=close_type
        )

    def on_checked(self, status):  # 选择二次确认
        global current_config
        current_config.get("main").update(
            second_confirm=status
        )

    def save_setting(self):  # 保存设置
        global current_config
        manager.save_(current_config)

    def closeEvent(self, event) -> None:
        self.save_setting()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    con = Common()
    sys.exit(app.exec())
