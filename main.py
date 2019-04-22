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



window = MainWindow()
window.show()

sys.exit(app.exec_())