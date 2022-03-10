from PyQt5.QtWidgets import QApplication

from controller.MenuController import MenuController
from controller.WindowController import WindowController
from controller.TextAreaController import TextAreaController
import sys


if __name__ == '__main__':
    # start application
    app = QApplication(sys.argv)

    # initialize program
    windowController = WindowController()
    win = windowController.window

    textAreaController = TextAreaController(win)
    menuController = MenuController(win)

    win.show()
    app.exec()

else:
    print("Bu program bir modül değildir.")
