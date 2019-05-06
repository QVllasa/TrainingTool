import glob
import sys
import os

from os import listdir
from os.path import isfile, join

from PyQt5.QtCore import *
from qtpy.QtWidgets import *

from ui.mainwindow import Ui_MainWindow
from PyPDF4 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from compressor import compress

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
        self.ui.addWat.clicked.connect(self.addWatermark)

    #   print(glob.glob('files/Material/*.pdf'))
    def addWatermark(self):
        self.obj = Worker('files/Material/PDF/'+str(self.ui.matCombo.currentText()))
        self.obj.start()

    def saveFiles(self):
        self.currentFile = self.ui.matCombo.currentText()
        for i in glob.glob('files/Material/PDF/*.pdf'):
            if self.currentFile in i:
                self.currentFile = i
                print(i)

    def addCell(self):
        row = self.ui.materialList.rowCount()
        self.ui.materialList.insertRow(row)

    def addFiles(self):
        self.onlyfiles = [f for f in listdir('files/Material/PDF/') if isfile(join('files/Material/PDF/', f))]
        self.ui.matCombo.addItems(self.onlyfiles)


class Worker(QThread):
    blabla = pyqtSignal(str)

    def __init__(self, filename):
        QThread.__init__(self)

        self.currentFile = filename

    def run(self) -> None:
        buffer = BytesIO()
        file = open(self.currentFile, 'rb')
        material = PdfFileReader(file)
        x = material.getPage(0).mediaBox[-2]
        y = material.getPage(0).mediaBox[-1]

        pageNum = material.getNumPages()

        p = canvas.Canvas(buffer)
        r = Color(0, 0, 0, alpha=0.5)
        p.setFont('Helvetica', 75)
        p.setFillColor(r)
        p.setPageSize((x, y))

        p.translate(x / 2, y / 2)
        p.rotate(45)
        p.drawCentredString(0, 0, "holaaaaaaaaaaaa")

        p.showPage()
        p.save()
        buffer.seek(0)

        watermark = PdfFileReader(buffer)
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        count = float(0)
        for page in range(pageNum):
            slide = material.getPage(page)
            slide.mergePage(watermark.getPage(0))
            slide.compressContentStreams()
            output.addPage(slide)
            count += float(100) / float(len(range(pageNum)))
            print(round(count))

        outputStream = open('output.pdf', 'wb')
        output.write(outputStream)
        outputStream.close()

        compress('output.pdf', 'output_mat.pdf', power=3)
        os.remove('output.pdf')


window = MainWindow()
window.show()

sys.exit(app.exec_())
