import sys

from PyQt5.QtCore import *
from qtpy.QtWidgets import *

from ui.mainwindow import Ui_MainWindow

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)



        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.addPart.clicked.connect(self.addCell)

    def addCell(self):
        row = self.ui.materialList.rowCount()
        self.ui.materialList.insertRow(row)


class Worker(QThread):
    blabla = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)

    def run(self) -> None:
        pass

window = MainWindow()
window.show()

sys.exit(app.exec_())