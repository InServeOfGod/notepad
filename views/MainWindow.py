from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super(MainWindow, self).__init__()

        self.controller = controller
        self.main_layout = QHBoxLayout(self)

    def main(self):
        self.setWindowTitle("Not Defteri")
        self.setMinimumSize(700, 700)
        self.setWindowIcon(QIcon("./assets/img/notebook.png"))
        self.setLayout(self.main_layout)
        self.show()
