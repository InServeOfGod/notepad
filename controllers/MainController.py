import time
from PyQt5.QtWidgets import QMessageBox, QDialog
from model.model import Model
from views.MainWindow import MainWindow
from views.Menus import Menus
from views.PrintDialog import PrintDialog
from views.TextArea import TextArea


class MainController:
    def __init__(self):
        self.model = Model()
        self.main_view = MainWindow(self)
        self.menu_view = Menus(self)
        self.text_view = TextArea(self)
        self.printer_view = PrintDialog(self)

    # initialize views

    def main(self) -> MainWindow:
        """
        ana pencere
        :rtype: MainWindow
        """
        self.main_view.main()
        return self.main_view

    def menu(self) -> Menus:
        """
        ana pencere menüleri
        :rtype: Menus
        """
        self.menu_view.add_menus()
        self.menu_view.add_actions()
        self.menu_view.triggers()
        self.menu_view.checks()
        self.menu_view.shortcuts()
        return self.menu_view

    def text_area(self) -> TextArea:
        """
        ana pencere yazı kısmı
        :rtype: TextArea
        """
        self.text_view.add()
        return self.text_view

    # action listeners

    def action_file_new(self):
        pass

    def action_file_new_window(self):
        pass

    def action_file_open(self):
        pass

    def action_file_save(self):
        pass

    def action_file_save_as(self):
        pass

    def action_file_print(self):
        if self.printer_view.exec() == QDialog.Accepted:
            self.text_view.print(self.printer_view.printer())

    def action_file_exit(self):
        confirm = QMessageBox.question(self.main_view, self.main_view.windowTitle(),
                                       "Yaptığınız değişiklikleri kaydetmek istiyor musunuz?",
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if confirm == QMessageBox.Cancel:
            return False

        # todo : save file
        if confirm == QMessageBox.Yes:
            print("file is saved")
            pass

        self.main_view.destroy(True, True)
        return True

    def action_edit_select_all(self):
        self.text_view.selectAll()

    def action_edit_undo(self):
        self.text_view.undo()

    def action_edit_redo(self):
        self.text_view.redo()

    def action_edit_cut(self):
        self.text_view.cut()

    def action_edit_copy(self):
        self.text_view.copy()

    def action_edit_paste(self):
        self.text_view.paste()

    def action_edit_find(self):
        # todo : make dialog box
        self.text_view.find("hey")

    def action_edit_replace(self):
        # todo : make dialog box
        pass

    def action_edit_datetime(self):
        self.text_view.insertPlainText(time.ctime())

    def action_view_full(self):
        if self.main_view.isFullScreen():
            self.main_view.showNormal()

        else:
            self.main_view.showFullScreen()

    def action_view_menu(self):
        menubar = self.main_view.menuBar()

        if menubar.isVisible():
            menubar.setVisible(False)

        else:
            menubar.setVisible(True)

    def action_view_toolbar(self):
        pass

    def action_settings_fg(self):
        pass

    def action_settings_bg(self):
        pass

    def action_settings_font(self):
        pass

    def action_help_help(self):
        # todo : make dialog box
        QMessageBox.information(self.main_view, self.main_view.windowTitle(),
                                "inserveofgod@gmail.com adresine mail gönderebilirsiniz", QMessageBox.Ok)

    def action_help_about(self):
        # todo : make dialog box
        QMessageBox.information(self.main_view, self.main_view.windowTitle(), "Bu program InServeOfGod tarafından yapıldı.",
                                QMessageBox.Ok)

