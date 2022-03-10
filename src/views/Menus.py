from PyQt5.QtWidgets import QMenu
from views.Actions import Actions


class Menus(Actions):
    def __init__(self):
        super(Menus, self).__init__()

        self.file = QMenu("&Dosya")
        self.edit = QMenu("Dü&zenle")
        self.view = QMenu("&Görünüm")
        self.settings = QMenu("&Ayarlar")
        self.help = QMenu("&Yardım")

        self.file.addAction(self.file_new)
        self.file.addAction(self.file_open)
        self.file.addAction(self.file_save)
        self.file.addAction(self.file_save_as)
        self.file.addAction(self.file_print)
        self.file.addAction(self.file_exit)

        self.edit.addAction(self.edit_select_all)
        self.edit.addAction(self.edit_undo)
        self.edit.addAction(self.edit_redo)
        self.edit.addAction(self.edit_cut)
        self.edit.addAction(self.edit_copy)
        self.edit.addAction(self.edit_paste)
        self.edit.addAction(self.edit_delete)
        self.edit.addAction(self.edit_backspace)
        self.edit.addAction(self.edit_find)
        self.edit.addAction(self.edit_replace)

        self.view.addAction(self.view_full)
        self.view.addAction(self.view_toggle_menu)
        self.view.addAction(self.view_toggle_toolbar)

        self.settings.addAction(self.settings_fg)
        self.settings.addAction(self.settings_bg)
        self.settings.addAction(self.settings_font)

        self.help.addAction(self.help_help)
        self.help.addAction(self.help_about)
