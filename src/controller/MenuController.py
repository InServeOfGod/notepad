from PyQt5.QtWidgets import QMainWindow
from views.Menus import Menus


class MenuController:
    def __init__(self, window: QMainWindow):
        self.window = window
        self.menus = Menus()

        self.menuBar = self.window.menuBar()

        self.menuBar.addMenu(self.menus.file)
        self.menuBar.addMenu(self.menus.edit)
        self.menuBar.addMenu(self.menus.view)
        self.menuBar.addMenu(self.menus.settings)
        self.menuBar.addMenu(self.menus.help)
