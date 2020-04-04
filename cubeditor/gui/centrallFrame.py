#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui.glib import customwidgets
from gui import centerViewFrame



class CentrallFrame(customwidgets.ToolTypeFrame):
    def __init__(self, name, main,  *args, **kwargs):
        super().__init__(name, *args, **kwargs)

        self.main = main
        # self.__initUi()

    def __initUi(self):
        self.box = customwidgets.BoxLayout(QBoxLayout.TopToBottom, self)
        self.VSplitter = QSplitter(Qt.Vertical)
        # self.VSplitter.setSizes([2,5,2])
        self.box.addWidget(self.VSplitter)
        self.graphicsView = QGraphicsView()
        self.graphicsView.setObjectName("graphicsView")
        self.topFrameCentral = customwidgets.ToolTypeFrame("topFrameCentral")
        self.topFrameCentral.setMinimumHeight(28)
        self.topFrameCentral.setMaximumHeight(150)
        self.centralHFrameCentral = customwidgets.ToolTypeFrame("centralHFrameCentral")
        self.centralHbox = customwidgets.BoxLayout(QBoxLayout.LeftToRight, self.centralHFrameCentral)
        self.bottomFrameCentral = customwidgets.ToolTypeFrame("bottomFrameCentral")
        self.bottomFrameCentral.setMinimumHeight(28)
        self.bottomFrameCentral.setMaximumHeight(150)

        self.VSplitter.addWidget(self.topFrameCentral)
        self.VSplitter.addWidget(self.centralHFrameCentral)
        self.VSplitter.addWidget(self.bottomFrameCentral)

        self.leftFrame = customwidgets.ToolTypeFrame("leftFrame")
        self.leftFrame.setMinimumWidth(28)
        self.leftFrame.setMaximumWidth(450)


        self.centerFrame = centerViewFrame.CenterViewFrame("centerFrame", self.main)

        self.rightFrame = customwidgets.ToolTypeFrame("rightFrame")
        self.rightFrame.setMinimumWidth(28)
        self.rightFrame.setMaximumWidth(450)


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