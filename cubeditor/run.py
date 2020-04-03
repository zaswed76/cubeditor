
from PyQt5 import QtWidgets
import sys
import paths
sys.path.insert(0, paths.ROOT)
from gui.main import Main



def main():

    app = QtWidgets.QApplication(sys.argv)
    main = Main(paths.MAIN_CONFIG, "main")
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()