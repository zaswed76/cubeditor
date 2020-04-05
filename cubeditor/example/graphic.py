#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Scene(QGraphicsScene):
    def __init__(self):
        super().__init__()


class View(QGraphicsView):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.resize(500, 500)

    def resizeEvent(self, Event):
        sceneRect = QRectF(QRect(self.rect().topLeft(), Event.size()))
        self.setSceneRect(sceneRect)



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralFrame = QFrame()
        self.box = QHBoxLayout(self.centralFrame)
        self.view = View()
        self.box.addWidget(self.view)
        self.setCentralWidget(self.centralFrame)

        self.scene = Scene()
        self.view.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Main()
    main.show()
    sys.exit(app.exec_())