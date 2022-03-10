from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction


class Actions:
    def __init__(self):
        self.file_new = QAction(QIcon("./assets/img/document--plus.png"), "Yeni")
        self.file_new.setShortcut(QKeySequence("Ctrl+N"))

        self.file_open = QAction(QIcon("./assets/img/document-import.png"), "Aç")
        self.file_open.setShortcut(QKeySequence("Ctrl+O"))

        self.file_save = QAction(QIcon("./assets/img/disk-return.png"), "Kaydet")
        self.file_save.setShortcut(QKeySequence("Ctrl+S"))

        self.file_save_as = QAction(QIcon("./assets/img/disks.png"), "Farklı Kaydet")
        self.file_save_as.setShortcut(QKeySequence("Ctrl+Shift+S"))

        self.file_print = QAction(QIcon("./assets/img/printer.png"), "Yazdır")
        self.file_print.setShortcut(QKeySequence("Ctrl+P"))

        self.file_exit = QAction(QIcon("./assets/img/door-open-in.png"), "Çık")
        self.file_exit.setShortcut(QKeySequence("Alt+F4"))

        self.edit_select_all = QAction(QIcon("./assets/img/selection-select.png"), "Hepsini Seç")
        self.edit_select_all.setShortcut(QKeySequence("Ctrl+A"))

        self.edit_undo = QAction(QIcon("./assets/img/arrow-turn-180-left.png"), "Geri al")
        self.edit_undo.setShortcut(QKeySequence("Ctrl+Z"))

        self.edit_redo = QAction(QIcon("./assets/img/arrow-turn.png"), "İleri al")
        self.edit_redo.setShortcut(QKeySequence("Ctrl+Y"))

        self.edit_cut = QAction(QIcon("./assets/img/scissors.png"), "Kes")
        self.edit_cut.setShortcut(QKeySequence("Ctrl+X"))

        self.edit_copy = QAction(QIcon("./assets/img/document-copy.png"), "Kopyala")
        self.edit_copy.setShortcut(QKeySequence("Ctrl+C"))

        self.edit_paste = QAction(QIcon("./assets/img/clipboard-paste.png"), "Yapıştır")
        self.edit_paste.setShortcut(QKeySequence("Ctrl+V"))

        self.edit_delete = QAction(QIcon("./assets/img/document-hf-delete.png"), "Sağdan Sil")
        self.edit_delete.setShortcut(QKeySequence("Del"))

        self.edit_backspace = QAction(QIcon("./assets/img/document-hf-delete-footer.png"), "Sil")
        self.edit_backspace.setShortcut(QKeySequence("Backspace"))

        self.edit_find = QAction(QIcon("./assets/img/magnifier.png"), "Bul")
        self.edit_find.setShortcut(QKeySequence("Ctrl+F"))

        self.edit_replace = QAction(QIcon("./assets/img/magnifier--pencil.png"), "Değiştir")
        self.edit_replace.setShortcut(QKeySequence("Ctrl+R"))

        self.view_full = QAction(QIcon("./assets/img/application-resize-full.png"), "Tam Ekran")
        self.view_full.setShortcut(QKeySequence("F+11"))

        self.view_toggle_menu = QAction(QIcon("./assets/img/ui-menu.png"), "Menü Göster/Gizle")
        self.view_toggle_menu.setShortcut(QKeySequence("Ctrl+Shift+M"))

        self.view_toggle_toolbar = QAction(QIcon("./assets/img/ui-toolbar.png"), "Araç Çubuğu Göster/Gizle")
        self.view_toggle_toolbar.setShortcut(QKeySequence("Ctrl+Shift+T"))

        self.settings_fg = QAction(QIcon("./assets/img/highlighter-color.png"), "Yazı Rengi")
        self.settings_fg.setShortcut(QKeySequence("Ctrl+Shift+T"))

        self.settings_bg = QAction(QIcon("./assets/img/paint-can-color.png"), "Arkaplan Rengi")
        self.settings_bg.setShortcut(QKeySequence("Ctrl+Shift+B"))

        self.settings_font = QAction(QIcon("./assets/img/layer-shape-text.png"), "Font Ayarları")
        self.settings_font.setShortcut(QKeySequence("Ctrl+Shift+F"))

        self.help_help = QAction(QIcon("./assets/img/question.png"), "Yardım")
        self.help_help.setShortcut(QKeySequence("Ctrl+H"))

        self.help_about = QAction(QIcon("./assets/img/information.png"), "Hakkında")
        self.help_about.setShortcut(QKeySequence("Ctrl+Shift+O"))
