from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow


class Base(QMainWindow):
    closed = Signal(str)

    def closeEvent(self, event):
        self.closed.emit(self.__class__.__name__)
        event.accept()
