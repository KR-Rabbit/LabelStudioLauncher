from menu import Base
from ui.Abort_UI import Ui_Abort


class Help(Base):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Abort()
        self.ui.setupUi(self)
        self.show()
