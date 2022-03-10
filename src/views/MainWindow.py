from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Not Defteri")
        self.setWindowIcon(QIcon("./assets/img/notebook.png"))
        self.setMinimumSize(700, 700)

        self.main_layout = QHBoxLayout(self)
        self.setLayout(self.main_layout)
