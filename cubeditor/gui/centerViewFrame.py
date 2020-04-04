#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui.glib import customwidgets

class Scene(QGraphicsScene):
    def __init__(self, *__args, **kwargs):
        super().__init__(*__args)
        self.model = kwargs.get("model", [])
        self.setBackgroundBrush(Qt.lightGray)

        self.item = QGraphicsRectItem(0, 0, 100, 100)
        self.item.setFlag(QGraphicsPixmapItem.ItemIsMovable)
        self.item.setFlag(QGraphicsPixmapItem.ItemIsSelectable)

    def updateItems(self):
        for i in self.model:
            self.addItem(i)


class View(QGraphicsView):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setDragMode(QGraphicsView.RubberBandDrag)

    def resizeEvent(self, QResizeEvent):
        self.setSceneRect(0, 0, QResizeEvent.size().width(), QResizeEvent.size().height())




class CenterViewFrame(customwidgets.ToolTypeFrame):
    def __init__(self, name, main, *args, **kwargs):

        super().__init__(name, *args, **kwargs)
        self.main = main
        self.box = customwidgets.BoxLayout(QBoxLayout.TopToBottom, self)
        self.view = View(self.main)
        self.scene = Scene()
        self.view.setScene(self.scene)
        self.box.addWidget(self.view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = CenterViewFrame("")
    main.show()
    sys.exit(app.exec_())