from PySide6.QtCore import QThread, Signal


class Executor(QThread):
    result_signal = Signal(object)

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        result = self.func(*self.args, **self.kwargs)
        self.result_signal.emit(result)
