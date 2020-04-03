#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui.glib import customwidgets

class View(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(Qt.gray)
        self.setScene(self.scene)

        self.item = QGraphicsRectItem(0, 0, 100, 100)
        self.scene.addItem(self.item)

        self.item.setFlag(QGraphicsPixmapItem.ItemIsMovable
                     )
        self.item.setFlag(QGraphicsPixmapItem.ItemIsSelectable)


    def resizeEvent(self, QResizeEvent):

        self.setSceneRect(0, 0, QResizeEvent.size().width(), QResizeEvent.size().height())
        self.ensureVisible(self.item)
        print(self.sceneRect())

class CenterViewFrame(customwidgets.ToolTypeFrame):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.box = customwidgets.BoxLayout(QBoxLayout.TopToBottom, self)

        self.view = View()
        self.box.addWidget(self.view)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = CenterViewFrame("")
    main.show()
    sys.exit(app.exec_())