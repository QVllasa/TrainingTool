import glob
import sys
import PyPDF4

from os import listdir
from os.path import isfile, join

from PyQt5.QtCore import *
from qtpy.QtWidgets import *

from ui.mainwindow import Ui_MainWindow

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.currentFile = ''

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.addFiles()
        self.ui.addPart.clicked.connect(self.addCell)
        self.ui.saveMat.clicked.connect(self.saveFiles)

    #   print(glob.glob('files/Material/*.pdf'))

    def saveFiles(self):
        self.currentFile = self.ui.matCombo.currentText()
        for i in glob.glob('files/Material/*.pdf'):
            if self.currentFile in i:
                self.currentFile = i
                print(i)

    def addCell(self):
        row = self.ui.materialList.rowCount()
        self.ui.materialList.insertRow(row)

    def addFiles(self):
        self.onlyfiles = [f for f in listdir('files/Material/') if isfile(join('files/Material', f))]
        self.ui.matCombo.addItems(self.onlyfiles)


class Worker(QThread):
    blabla = pyqtSignal(str)

    def __init__(self, filename, ):
        QThread.__init__(self)

        self.currentFile = filename

    def run(self) -> None:
        pass
        # material = open(self.currentFile, 'rb')
        # pdfReader = PyPDF4.PdfFileReader(material)
        # output = PyPDF4.PdfFileWriter()



window = MainWindow()
window.show()

sys.exit(app.exec_())
