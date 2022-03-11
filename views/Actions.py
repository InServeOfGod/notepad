from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import QAction


class Actions:
    def __init__(self, controller):
        self.controller = controller

        self.file_new = QAction(QIcon("./assets/img/document--plus.png"), "Yeni")
        self.file_new_window = QAction(QIcon("./assets/img/newspapers.png"), "Yeni Pencere")
        self.file_open = QAction(QIcon("./assets/img/document-import.png"), "Aç")
        self.file_save = QAction(QIcon("./assets/img/disk-return.png"), "Kaydet")
        self.file_save_as = QAction(QIcon("./assets/img/disks.png"), "Farklı Kaydet")
        self.file_print = QAction(QIcon("./assets/img/printer.png"), "Yazdır")
        self.file_exit = QAction(QIcon("./assets/img/door-open-in.png"), "Çık")

        self.edit_select_all = QAction(QIcon("./assets/img/selection-select.png"), "Hepsini Seç")
        self.edit_undo = QAction(QIcon("./assets/img/arrow-turn-180-left.png"), "Geri al")
        self.edit_redo = QAction(QIcon("./assets/img/arrow-turn.png"), "İleri al")
        self.edit_cut = QAction(QIcon("./assets/img/scissors.png"), "Kes")
        self.edit_copy = QAction(QIcon("./assets/img/document-copy.png"), "Kopyala")
        self.edit_paste = QAction(QIcon("./assets/img/clipboard-paste.png"), "Yapıştır")
        self.edit_find = QAction(QIcon("./assets/img/magnifier.png"), "Bul")
        self.edit_replace = QAction(QIcon("./assets/img/magnifier--pencil.png"), "Değiştir")
        self.edit_datetime = QAction(QIcon("./assets/img/sort-date.png"), "Tarih & Saat")

        self.view_full = QAction(QIcon("./assets/img/application-resize-full.png"), "Tam Ekran")
        self.view_toggle_menu = QAction(QIcon("./assets/img/ui-menu.png"), "Menü Göster/Gizle")
        self.view_toggle_toolbar = QAction(QIcon("./assets/img/ui-toolbar.png"), "Araç Çubuğu Göster/Gizle")

        self.settings_fg = QAction(QIcon("./assets/img/highlighter-color.png"), "Yazı Rengi")
        self.settings_bg = QAction(QIcon("./assets/img/paint-can-color.png"), "Arkaplan Rengi")
        self.settings_font = QAction(QIcon("./assets/img/layer-shape-text.png"), "Font Ayarları")

        self.help_help = QAction(QIcon("./assets/img/question.png"), "Yardım")
        self.help_about = QAction(QIcon("./assets/img/information.png"), "Hakkında")

    def shortcuts(self):
        self.file_new.setShortcut(QKeySequence("Ctrl+N"))
        self.file_new_window.setShortcut(QKeySequence("Ctrl+Shift+N"))
        self.file_open.setShortcut(QKeySequence("Ctrl+O"))
        self.file_save.setShortcut(QKeySequence("Ctrl+S"))
        self.file_save_as.setShortcut(QKeySequence("Ctrl+Shift+S"))
        self.file_print.setShortcut(QKeySequence("Ctrl+P"))
        self.file_exit.setShortcut(QKeySequence("Alt+F4"))

        self.edit_select_all.setShortcut(QKeySequence("Ctrl+A"))
        self.edit_undo.setShortcut(QKeySequence("Ctrl+Z"))
        self.edit_redo.setShortcut(QKeySequence("Ctrl+Y"))
        self.edit_cut.setShortcut(QKeySequence("Ctrl+X"))
        self.edit_copy.setShortcut(QKeySequence("Ctrl+C"))
        self.edit_paste.setShortcut(QKeySequence("Ctrl+V"))
        self.edit_find.setShortcut(QKeySequence("Ctrl+F"))
        self.edit_replace.setShortcut(QKeySequence("Ctrl+R"))
        self.edit_datetime.setShortcut(QKeySequence("F5"))

        self.view_full.setShortcut(QKeySequence("F11"))
        self.view_toggle_menu.setShortcut(QKeySequence("Ctrl+Shift+M"))
        self.view_toggle_toolbar.setShortcut(QKeySequence("Ctrl+Shift+T"))

        self.settings_fg.setShortcut(QKeySequence("Ctrl+Shift+T"))
        self.settings_bg.setShortcut(QKeySequence("Ctrl+Shift+B"))
        self.settings_font.setShortcut(QKeySequence("Ctrl+Shift+F"))

        self.help_help.setShortcut(QKeySequence("Ctrl+H"))
        self.help_about.setShortcut(QKeySequence("Ctrl+Shift+O"))

    def checks(self):
        self.view_full.setCheckable(True)
        self.view_full.setChecked(False)

        self.view_toggle_menu.setCheckable(True)
        self.view_toggle_menu.setChecked(True)

        self.view_toggle_toolbar.setCheckable(True)
        self.view_toggle_toolbar.setChecked(True)

    def triggers(self):
        self.file_new.triggered.connect(self.controller.action_file_new)
        self.file_new_window.triggered.connect(self.controller.action_file_new)
        self.file_open.triggered.connect(self.controller.action_file_open)
        self.file_save.triggered.connect(self.controller.action_file_save)
        self.file_save_as.triggered.connect(self.controller.action_file_save_as)
        self.file_print.triggered.connect(self.controller.action_file_print)
        self.file_exit.triggered.connect(self.controller.action_file_exit)

        self.edit_select_all.triggered.connect(self.controller.action_edit_select_all)
        self.edit_undo.triggered.connect(self.controller.action_edit_undo)
        self.edit_redo.triggered.connect(self.controller.action_edit_redo)
        self.edit_cut.triggered.connect(self.controller.action_edit_cut)
        self.edit_copy.triggered.connect(self.controller.action_edit_copy)
        self.edit_paste.triggered.connect(self.controller.action_edit_paste)
        self.edit_find.triggered.connect(self.controller.action_edit_find)
        self.edit_replace.triggered.connect(self.controller.action_edit_replace)
        self.edit_datetime.triggered.connect(self.controller.action_edit_datetime)

        self.view_full.triggered.connect(self.controller.action_view_full)
        self.view_toggle_menu.triggered.connect(self.controller.action_view_menu)
        self.view_toggle_toolbar.triggered.connect(self.controller.action_view_toolbar)

        self.settings_fg.triggered.connect(self.controller.action_settings_fg)
        self.settings_bg.triggered.connect(self.controller.action_settings_bg)
        self.settings_font.triggered.connect(self.controller.action_settings_font)

        self.help_help.triggered.connect(self.controller.action_help_help)
        self.help_about.triggered.connect(self.controller.action_help_about)
