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
        self.path = 'files/Material/PDF/'
        self.participantList = []



        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.addFiles()
        self.ui.addPart.clicked.connect(self.addCell)
       # self.ui.saveMat.clicked.connect(self.saveFiles)
        self.ui.addWat.clicked.connect(self.addWatermark)

    #   print(glob.glob('files/Material/*.pdf'))
    def addWatermark(self):
        self.getParticipants()
        self.currentFile = self.ui.matCombo.currentText()


        #for i in self.participantList:
         #   print(i)


        print(self.path+self.currentFile)

        self.obj = MWorker(self.path, self.currentFile, self.participantList)
        #self.obj.start()

    def getParticipants(self):
        for i in range(0,self.ui.participants.rowCount()):
            self.participant = Participant()
            if not self.ui.participants.item(i, 2) == None:
                self.participant.firstname = self.ui.participants.item(i, 0).text()
                self.participant.lastname = self.ui.participants.item(i, 1).text()
                self.participant.email = self.ui.participants.item(i, 2).text()
                self.participantList.append(self.participant)


                #print(self.participant.firstname, self.participant.lastname, self.participant.email)

        for s in self.participantList:
            print(s)


    # def saveFiles(self):
    #     self.currentFile = self.ui.matCombo.currentText()

    def addCell(self):
        row = self.ui.participants.rowCount()
        self.ui.participants.insertRow(row)

    def addFiles(self):
        self.onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        self.ui.matCombo.addItems(self.onlyfiles)

class Participant():
    def __init__(self):

        self.firstname = ''
        self.lastname = ''
        self.email = ''

    def __repr__(self):
        return self.firstname+'  '+self.lastname+'  '+self.email

class MWorker(QThread):
    blabla = pyqtSignal(str)

    def __init__(self,path, filename, plist):
        QThread.__init__(self)

        self.currentFile = filename
        self.plist = plist
        self.path = path
        self.buffer = BytesIO()
        self.file = open(str(self.path)+str(self.currentFile), 'rb')
        self.material = PdfFileReader(self.file)
        self.x = self.material.getPage(0).mediaBox[-2]
        self.y = self.material.getPage(0).mediaBox[-1]
        self.pageNum = self.material.getNumPages()
        self.p = canvas.Canvas(self.buffer)
        self.r = Color(0, 0, 0, alpha=0.5)
        self.p.setFont('Helvetica', 75)
        self.p.setFillColor(self.r)
        self.p.setPageSize((self.x, self.y))
        self.p.translate(self.x / 2, self.y / 2)
        self.p.rotate(45)

    def run(self):
        for participant in self.plist:

            self.p.drawCentredString(0, 0, str(participant.email))
            self.p.showPage()
            self.p.save()
            self.buffer.seek(0)

            watermark = PdfFileReader(self.buffer)
            output = PdfFileWriter()
            # add the "watermark" (which is the new pdf) on the existing page
            count = float(0)
            for page in range(self.pageNum):
                slide = self.material.getPage(page)
                slide.mergePage(watermark.getPage(0))
                slide.compressContentStreams()
                output.addPage(slide)
                count += float(100) / float(len(range(self.pageNum)))
                print(round(count))

            outputStream = open('output.pdf', 'wb')
            output.write(outputStream)
            outputStream.close()
            print('hierhierhiehirhierhier')
            compress('output.pdf', 'output_'+str(participant.email)+'.pdf', power=3)
            os.remove('output.pdf')



window = MainWindow()
window.show()

sys.exit(app.exec_())
