from PyQt5.QtWidgets import QPlainTextEdit


class TextArea(QPlainTextEdit):
    def __init__(self, controller):
        super(TextArea, self).__init__()

        self.controller = controller
        self.win = self.controller.main_view

    def add(self):
        self.win.layout().addWidget(self)
        self.win.setCentralWidget(self)
