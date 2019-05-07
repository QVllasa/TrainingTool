import glob
import sys
import os
import shutil

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
        self.ui.saveMat.clicked.connect(self.saveFiles)
        self.ui.addWat.clicked.connect(self.addWatermark)

    #   print(glob.glob('files/Material/*.pdf'))
    def addWatermark(self):

        self.ui.participants.clearSelection()
        self.getParticipants()
        self.currentFile = self.ui.matCombo.currentText()

        self.obj = MWorker(self.path, self.currentFile, self.participantList)
        self.obj.finish.connect(self.disableEnable)
        self.obj.progress.connect(self.progressing)
        self.obj.start()

    def disableEnable(self, str):
        if str == 'begin':
            self.ui.addPart.setEnabled(False)

        if str == 'finished':
            self.ui.participants.setEnabled(True)
            self.ui.addPart.setEnabled(True)

    def progressing(self, count):
        self.ui.progressBarMat.setValue(count)

    def getParticipants(self):
        self.ui.participants.setEnabled(False)
        for i in range(0, self.ui.participants.rowCount()):
            self.participant = Participant()
            if self.ui.participants.item(i, 2):
                self.participant.firstname = self.ui.participants.item(i, 0).text()
                self.participant.lastname = self.ui.participants.item(i, 1).text()
                self.participant.email = self.ui.participants.item(i, 2).text()
                self.participantList.append(self.participant)

                # print(self.participant.firstname, self.participant.lastname, self.participant.email)

        for s in self.participantList:
            print(s)

    def saveFiles(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory")+'/')
        temp = 'temp/'
        onlyfiles = [f for f in listdir(temp) if isfile(join(temp, f))]
        for i in onlyfiles:
            #print(temp + i)
            #print(file + i)
            shutil.move(temp + i, file + i)

    def addCell(self):
        self.ui.participants.setEnabled(True)
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
        return self.firstname + '  ' + self.lastname + '  ' + self.email


class MWorker(QThread):
    progress = pyqtSignal(float)

    finish = pyqtSignal(str)

    def __init__(self, path, filename, plist):
        QThread.__init__(self)

        self.currentFile = filename
        self.plist = plist
        self.path = path

    def run(self):
        self.finish.emit('begin')

        count = float(0)
        self.progress.emit(count)
        for participant in self.plist:

            self.buffer = BytesIO()
            self.file = open(str(self.path) + str(self.currentFile), 'rb')
            self.material = PdfFileReader(self.file)
            self.x = float(self.material.getPage(0).mediaBox[-2])
            self.y = float(self.material.getPage(0).mediaBox[-1])
            self.pageNum = self.material.getNumPages()
            self.p = canvas.Canvas(self.buffer)
            self.r = Color(0, 0, 0, alpha=0.5)
            self.p.setFont('Helvetica', 75)
            self.p.setFillColor(self.r)
            self.p.setPageSize((self.x, self.y))
            self.p.translate(self.x / float(2), self.y / float(2))
            self.p.rotate(45)

            self.p.drawCentredString(0, 0, str(participant.email))
            self.p.showPage()
            self.p.save()
            self.buffer.seek(0)

            watermark = PdfFileReader(self.buffer)
            output = PdfFileWriter()
            # add the "watermark" (which is the new pdf) on the existing page

            for page in range(self.pageNum):
                slide = self.material.getPage(page)
                slide.mergePage(watermark.getPage(0))
                slide.compressContentStreams()
                output.addPage(slide)
                count += (float(100) / float(len(self.plist))) / float(len(range(self.pageNum)))
                print(round(count))
                self.progress.emit(count)

            newfile = self.currentFile.replace('.pdf', '')

            #outputStream = open('output.pdf', 'wb')
            outputStream = open('temp/' + str(newfile) + '_' + str(participant.email) + '.pdf', 'wb')
            output.write(outputStream)
            outputStream.close()
            #compress('output.pdf', 'temp/' + str(newfile) + '_' + str(participant.email) + '.pdf', power=0)
            #os.remove('output.pdf')

        self.finish.emit('finished')
        count = float(0)
        self.progress.emit(count)


window = MainWindow()
window.show()

sys.exit(app.exec_())


#TODO
#programm nicht schließbar, ohne dass man save bei Material/Certificate geklickt hat
