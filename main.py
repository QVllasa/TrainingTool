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

        #self.obj = Worker(self.path, self.currentFile, self.participantList)
        #self.obj.start()

    def getParticipants(self):
        for i in range(0,self.ui.participants.rowCount()):
            self.participant = Participant()
            if not self.ui.participants.item(i, 0) == None:
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

class Worker(QThread):
    blabla = pyqtSignal(str)

    def __init__(self,path, filename, plist):
        QThread.__init__(self)

        self.currentFile = filename
        self.plist = plist
        self.path = path

    def run(self) -> None:
        for participant in self.plist:
            if participant.email:
                buffer = BytesIO()
                file = open(self.path+self.currentFile, 'rb')
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
                p.drawCentredString(0, 0, participant.email)

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
                print('hierhierhiehirhierhier')
                compress('output.pdf', 'output_'+participant.email+'.pdf', power=3)
                os.remove('output.pdf')
            else: print('empty email')


window = MainWindow()
window.show()

sys.exit(app.exec_())
