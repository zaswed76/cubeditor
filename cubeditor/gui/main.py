#!/usr/bin/env python3

import sys
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import paths
from config import Config
from libs import filesTool
from gui import mainmenu
from gui import centrallFrame

class InsertToolBar(QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedHeight(42)
        self.addAction(QAction("img", self))









class Main(QMainWindow):
    def __init__(self, config_path, object_name=None):
        super().__init__()
        self.setObjectName(object_name)
        self.setToolTip(f"{self.__class__}")
        self.cfg = Config(config_path)
        self._setStylSheet(self.cfg["currentStyle"])
        self.__initUi()

    def __initUi(self):
        self.centralFrame = centrallFrame.CentrallFrame("centralFrame", self)
        self.setCentralWidget(self.centralFrame)

        self.menuBar = mainmenu.MainMenuBar()
        self.menuBar.setObjectName("menuBar")
        self.setMenuBar(self.menuBar)

        self.insertToolBar = InsertToolBar()
        self.insertToolBar.actionTriggered.connect(self.insertToolaction)
        self.addToolBar(self.insertToolBar)

        # self.gameToolBar = GameToolBar()
        # self.insertToolBar.actionTriggered.connect(self.insertToolaction)
        # self.addToolBar(Qt.RightToolBarArea, self.gameToolBar)

        # self.gameToolBar2 = GameToolBar()
        #
        # self.addToolBar(Qt.RightToolBarArea, self.gameToolBar2)

    def insertToolaction(self, action):
        print(action.text())




    def _setStylSheet(self, sheetName):
        """
        :param sheetName: str имя стиля
        """
        css_folder = str(paths.CSS_FOLDER / sheetName)
        styleSheet = filesTool.fileInput(css_folder)
        QApplication.instance().setStyleSheet(styleSheet)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.insertToolBar.setVisible(not self.insertToolBar.isVisible())
            self.gameToolBar.setVisible(not self.gameToolBar.isVisible())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Main()
    main.show()
    sys.exit(app.exec_())