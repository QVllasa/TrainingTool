import glob
import sys
import shutil
import os

from os import listdir
from os.path import isfile, join

from PyQt5.QtCore import *
from qtpy.QtWidgets import *

from ui.mainwindow import Ui_MainWindow
from ui.addLocationDialog import Ui_LocationDialog
from ui.addTrainerDialog import Ui_TrainerDialog
from ui.LocationListDialog import Ui_RemoveLocationDialog
from ui.trainerListDialog import Ui_RemoveTrainerDialog
from PyPDF4 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from generateCertificate import generateCertificate
from compressor import compress

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.configFile = 'config.txt'
        self.currentFile = ''
        self.materialPath = 'files/Material/PDF/'
        self.certificatePath = 'files/Certificates/'
        self.participantList = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.getComboBoxes()

        self.getComboBoxes()
        self.ui.addPart.clicked.connect(self.addCell)
        self.ui.saveMat.clicked.connect(self.saveFiles)
        self.ui.addWat.clicked.connect(self.addWatermark)
        self.ui.generateCert.clicked.connect(self.genCertificate)
        self.ui.addLocation.clicked.connect(self.addingLocation)
        self.ui.addTrainer.clicked.connect(self.addingTrainer)
        self.ui.addMaterial.clicked.connect(self.addingMaterial)
        self.ui.removeTrainer.clicked.connect(self.removingTrainer)
        self.ui.removeLocation.clicked.connect(self.removingLocation)

    #   print(glob.glob('files/Material/*.pdf'))

    def genCertificate(self):

        self.getParticipants()
        dateTo = self.ui.certDateTo.text()
        dateFrom = self.ui.certDateFrom.text()

        if dateFrom:
            date = dateFrom + '.' + ' - ' + dateTo
        else:
            date = dateTo


        path = self.certificatePath
        filename = self.ui.certCombo.currentText()
        location = self.ui.locationCombo.currentText()

        self.obj = CWorker(self.participantList, date, location, path, filename)
        self.obj.finish.connect(self.disableEnable)
        self.obj.progress.connect(self.progressing)
        self.obj.start()

    def removingLocation(self):
        self.remLocationDialog = QDialog()
        self.uiRemLocationDialog = Ui_RemoveLocationDialog()
        self.uiRemLocationDialog.setupUi(self.remLocationDialog)
        self.remLocationDialog.show()

        AllItemsLocation = [self.ui.locationCombo.itemText(i) for i in range(self.ui.locationCombo.count())]
        for i in AllItemsLocation:
            row = self.uiRemLocationDialog.locationList.rowCount()
            self.uiRemLocationDialog.locationList.insertRow(row)
            self.uiRemLocationDialog.locationList.setItem(row, 0, QTableWidgetItem(str(i)))

        self.uiRemLocationDialog.removeButton.clicked.connect(self.removeLocationItem)
        self.uiRemLocationDialog.cancelButton.clicked.connect(self.remLocationDialog.reject)

        self.getComboBoxes()

    def removeLocationItem(self):
        row = self.uiRemLocationDialog.locationList.rowCount()
        if not row == None:
            self.ui.locationCombo.clear()
            item = self.uiRemLocationDialog.locationList.currentItem().text()
            f = open(self.configFile, "r")
            contents = f.readlines()
            f.close()
            print('remove pressed')

            for i in contents:
                if item in i:
                    contents.remove(i)
                    for j in range(0, row):
                        if item in self.uiRemLocationDialog.locationList.item(j, 0).text():
                            print(item)

                else:
                    continue

            selected = self.uiRemLocationDialog.locationList.currentRow()
            self.uiRemLocationDialog.locationList.removeRow(selected)

            f = open(self.configFile, "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
        self.getComboBoxes()

    def addingLocation(self):
        self.locationDialog = QDialog()
        self.uiLocationDialog = Ui_LocationDialog()
        self.uiLocationDialog.setupUi(self.locationDialog)
        self.locationDialog.show()
        rsp = self.locationDialog.exec_()
        if rsp == 1:
            f = open(self.configFile, "r")
            contents = f.readlines()
            f.close()

            for i in contents:
                if 'location' in i:
                    index = contents.index(i)
                elif 'trainer' in i:
                    continue
            if not self.uiLocationDialog.locationInput.text() in contents:
                contents.insert(index + 1, self.uiLocationDialog.locationInput.text() + '\n')

            f = open(self.configFile, "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
        self.getComboBoxes()

    def removingTrainer(self):
        self.remTrainerDialog = QDialog()
        self.uiRemTrainerDialog = Ui_RemoveTrainerDialog()
        self.uiRemTrainerDialog.setupUi(self.remTrainerDialog)
        self.remTrainerDialog.show()

        AllItemsTrainer = [self.ui.trainerCombo.itemText(i) for i in range(self.ui.trainerCombo.count())]
        for i in AllItemsTrainer:
            row = self.uiRemTrainerDialog.trainerList.rowCount()
            self.uiRemTrainerDialog.trainerList.insertRow(row)
            self.uiRemTrainerDialog.trainerList.setItem(row, 0, QTableWidgetItem(str(i)))

        self.uiRemTrainerDialog.removeButton.clicked.connect(self.removeTrainerItem)
        self.uiRemTrainerDialog.cancelButton.clicked.connect(self.remTrainerDialog.reject)

        self.getComboBoxes()

    def removeTrainerItem(self):
        row = self.uiRemTrainerDialog.trainerList.rowCount()
        if not row == None:
            self.ui.trainerCombo.clear()
            item = self.uiRemTrainerDialog.trainerList.currentItem().text()
            f = open(self.configFile, "r")
            contents = f.readlines()
            f.close()
            print('remove pressed')

            for i in contents:
                if item in i:
                    for j in range(0, row):
                        if item in self.uiRemTrainerDialog.trainerList.item(j, 0).text():
                            print(item)
                            contents.remove(i)
                else:
                    continue

            selected = self.uiRemTrainerDialog.trainerList.currentRow()
            self.uiRemTrainerDialog.trainerList.removeRow(selected)

            f = open(self.configFile, "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
        self.getComboBoxes()

    def addingTrainer(self):
        self.trainerDialog = QDialog()
        self.uiTrainerDialog = Ui_TrainerDialog()
        self.uiTrainerDialog.setupUi(self.trainerDialog)
        self.trainerDialog.show()
        rsp = self.trainerDialog.exec_()
        if rsp == 1:
            f = open(self.configFile, "r")
            contents = f.readlines()
            f.close()

            for i in contents:
                if 'trainer' in i:
                    index = contents.index(i)
                elif 'location' in i:
                    continue
            if not self.uiTrainerDialog.trainerInput.text() in contents:
                contents.insert(index + 1, self.uiTrainerDialog.trainerInput.text() + '\n')

            f = open(self.configFile, "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()
        self.getComboBoxes()

    def getComboBoxes(self):
        self.ui.matCombo.clear()
        self.ui.certCombo.clear()

        certificateFiles = [f for f in listdir(self.certificatePath) if isfile(join(self.certificatePath, f))]
        materialFiles = [f for f in listdir(self.materialPath) if isfile(join(self.materialPath, f))]
        self.ui.matCombo.addItems(materialFiles)
        self.ui.certCombo.addItems(certificateFiles)
        AllItemsTrainer = [self.ui.trainerCombo.itemText(i) for i in range(self.ui.trainerCombo.count())]
        AllItemsLocation = [self.ui.locationCombo.itemText(i) for i in range(self.ui.locationCombo.count())]

        with open('config.txt', 'r') as file:
            x = int
            b = int
            y = int
            lines = file.readlines()
            for i in lines:
                if 'trainer' in i: x = lines.index(i)
                if len(i.strip()) == 0: b = lines.index(i)
                if 'location' in i: y = lines.index(i)

            for j in lines[x + 1:b]:
                if not j.strip() in AllItemsTrainer:
                    self.ui.trainerCombo.addItem(j.strip())
                else:
                    continue

            for j in lines[y + 1:]:
                if not j.strip() in AllItemsLocation:
                    self.ui.locationCombo.addItem(j.strip())
                else:
                    continue

    def addWatermark(self):

        self.ui.participants.clearSelection()
        self.getParticipants()
        self.currentFile = self.ui.matCombo.currentText()

        self.obj = MWorker(self.materialPath, self.currentFile, self.participantList)
        self.obj.finish.connect(self.disableEnable)
        self.obj.progress.connect(self.progressing)
        self.obj.start()

    def addingMaterial(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setLabelText(QFileDialog.Accept, 'import')
        if dialog.exec_():
            fname = dialog.selectedFiles()

        path, name = os.path.split(fname[0])
        if fname[0]:
            shutil.copyfile(fname[0], self.materialPath + name)
        self.getComboBoxes()

    def addingCertificate(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setLabelText(QFileDialog.Accept, 'import')
        if dialog.exec_():
            fname = dialog.selectedFiles()

        path, name = os.path.split(fname[0])
        if fname[0]:
            shutil.copyfile(fname[0], self.certificatePath + name)
        self.getComboBoxes()

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
 #TODO
            for j in self.participantList:
                if j.email == self.participant.email:

                    print('schon drin')
                    self.participantList.append(self.participant)
            else: continue

        for s in self.participantList:
            print(s)

    def saveFiles(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory") + '/')
        temp = 'temp/'
        onlyfiles = [f for f in listdir(temp) if isfile(join(temp, f))]
        for i in onlyfiles:
            shutil.move(temp + i, file + i)

    def addCell(self):
        self.ui.participants.setEnabled(True)
        row = self.ui.participants.rowCount()
        self.ui.participants.insertRow(row)


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
        self.materialPath = path

    def run(self):
        self.finish.emit('begin')

        count = float(0)
        self.progress.emit(count)
        for participant in self.plist:

            self.buffer = BytesIO()
            self.file = open(str(self.materialPath) + str(self.currentFile), 'rb')
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

            outputStream = open('temp/mat/' + str(newfile) + '_' + str(participant.email) + '.pdf', 'wb')
            output.write(outputStream)
            outputStream.close()
            # compress('output.pdf', 'temp/' + str(newfile) + '_' + str(participant.email) + '.pdf', power=0)
            # os.remove('output.pdf')

        self.finish.emit('finished')
        count = float(0)
        self.progress.emit(count)


class CWorker(QThread):
    progress = pyqtSignal(float)
    finish = pyqtSignal(str)

    def __init__(self, participants, date, location, path, filename):
        QThread.__init__(self)

        self.participants = participants

    def run(self):
        for i in self.participants:
            print(i)
        print('ENDE')
        # generateCertificate()


window = MainWindow()
window.show()

sys.exit(app.exec_())

# TODO
# programm nicht schließbar, ohne dass man save bei Material/Certificate geklickt hat
