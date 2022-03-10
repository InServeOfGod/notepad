from views.TextArea import TextArea
from PyQt5.QtWidgets import QMainWindow


class TextAreaController:
    def __init__(self, window: QMainWindow):
        super(TextAreaController, self).__init__()

        self.textArea = TextArea()
        self.window = window

        self.window.layout().addWidget(self.textArea.plain_text_edit)
        self.window.setCentralWidget(self.textArea.plain_text_edit)

    def import_settings(self):
        pass
