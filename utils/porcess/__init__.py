from PySide6.QtCore import QProcess, QObject, Signal


class Process(QObject):
    ready_signal = Signal(str)

    def __init__(self, program: str, arguments):
        super().__init__()
        self.program = program
        self.arguments = arguments
        self.process = QProcess()

    def start(self):
        self.process.start(self.program, self.arguments)
        # self.process.readyRead.connect(lambda: self.ready_signal.emit(self.process.readAll().data().strip().decode()))

    def stop(self):
        self.process.close()

    @property
    def finished(self):
        return self.process.finished

    @property
    def readyRead(self):
        return self.process.readyRead

    @property
    def info(self) -> str:
        return self.process.readAll().data().strip().decode()

    @property
    def error_info(self):
        return self.process.readAllStandardOutput().data().strip().decode()

    @property
    def readyReadStandardOutput(self):
        return self.process.readyReadStandardOutput

    def close(self):
        self.process.close()
