#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui.glib import customwidgets



class CentrallFrame(customwidgets.ToolTypeFrame):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)

        self.__initUi()

    def __initUi(self):
        self.box = customwidgets.BoxLayout(QBoxLayout.TopToBottom, self)
        self.VSplitter = QSplitter(Qt.Vertical)
        self.box.addWidget(self.VSplitter)
        self.graphicsView = QGraphicsView()
        self.graphicsView.setObjectName("graphicsView")
        self.topFrameCentral = customwidgets.ToolTypeFrame("topFrameCentral")
        self.centralHFrameCentral = customwidgets.ToolTypeFrame("centralHFrameCentral")
        self.centralHbox = customwidgets.BoxLayout(QBoxLayout.LeftToRight, self.centralHFrameCentral)
        self.bottomFrameCentral = customwidgets.ToolTypeFrame("bottomFrameCentral")

        self.VSplitter.addWidget(self.topFrameCentral)
        self.VSplitter.addWidget(self.centralHFrameCentral)
        self.VSplitter.addWidget(self.bottomFrameCentral)

        self.leftFrame = customwidgets.ToolTypeFrame("leftFrame")
        self.centerFrame = customwidgets.ToolTypeFrame("centerFrame")
        self.rightFrame = customwidgets.ToolTypeFrame("rightFrame")
        self.HSplitter = QSplitter(Qt.Horizontal)
        self.centralHbox.addWidget(self.HSplitter)
        self.HSplitter.addWidget(self.leftFrame)
        self.HSplitter.addWidget(self.centerFrame)
        self.HSplitter.addWidget(self.rightFrame)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())