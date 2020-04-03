#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class MainMenuBar(QMenuBar):
    def __init__(self):
        super().__init__()

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        fileMenu = self.addMenu('&File')
        fileMenu.addAction(exitAction)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = MainMenuBar()
    main.show()
    sys.exit(app.exec_())