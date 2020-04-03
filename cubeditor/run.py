
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import sys
import paths
sys.path.insert(0, paths.ROOT)
from gui.main import Main

def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'INFO'
    elif mode == QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))

qInstallMessageHandler(qt_message_handler)


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = Main(paths.MAIN_CONFIG, "main")
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()