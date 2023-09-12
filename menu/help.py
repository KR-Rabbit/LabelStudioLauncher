from PySide6.QtWidgets import QMainWindow

from ui.Abort_UI import Ui_Abort


class Help(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Abort()
        self.ui.setupUi(self)
        self.show()
