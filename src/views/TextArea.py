from PyQt5.QtWidgets import QPlainTextEdit


class TextArea(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super(TextArea, self).__init__(*args, **kwargs)
        self.plain_text_edit = self

