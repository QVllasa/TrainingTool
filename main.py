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
        self.materialPath = 'files/Material/'
        self.certificatePath = 'files/Certificates/'
        self.participantList = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.getComboBoxes()

        self.ui.trainingType.currentTextChanged.connect(self.onTrainingTypeChange)

        self.ui.addPart.clicked.connect(self.addCell)
        self.ui.saveMat.clicked.connect(self.saveMaterialFiles)
        self.ui.saveCert.clicked.connect(self.saveCertificationFiles)
        self.ui.addWat.clicked.connect(self.addWatermark)
        self.ui.generateCert.clicked.connect(self.genCertificate)
        self.ui.addLocation.clicked.connect(self.addingLocation)
        self.ui.addTrainer.clicked.connect(self.addingTrainer)
        self.ui.addMaterial.clicked.connect(self.addingMaterial)
        self.ui.addCertificate.clicked.connect(self.addingCertificate)
        self.ui.removeTrainer.clicked.connect(self.removingTrainer)
        self.ui.removeLocation.clicked.connect(self.removingLocation)

    #   print(glob.glob('files/Material/*.pdf'))
    def onTrainingTypeChange(self):
        if self.ui.trainingType.currentText() == 'Webinar':
            self.ui.locationCombo.setEnabled(False)
        else: self.ui.locationCombo.setEnabled(True)

    def genCertificate(self):

        self.getParticipants()
        dateTo = self.ui.certDateTo.text()
        if self.ui.certDateFrom.isEnabled():
            dateFrom = self.ui.certDateFrom.text()
            date = dateFrom + '.' + ' - ' + dateTo
        else:
            date = dateTo

        path = self.certificatePath
        filename = self.ui.certCombo.currentText()
        if self.ui.locationCombo.isEnabled():
            location = self.ui.locationCombo.currentText()
        else: location = ''

        trainer = self.ui.trainerCombo.currentText()


        obj = CWorker(self.participantList, date, location, path, filename, trainer)
        obj.finish.connect(self.disableEnableCertification)
        obj.progress.connect(self.progressingCertification)
        obj.start()

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

        obj = MWorker(self.materialPath, self.currentFile, self.participantList)
        obj.finish.connect(self.disableEnableParticipantList)
        obj.progress.connect(self.progressingMaterial)
        obj.start()

    def addingMaterial(self):
        fname = ''
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setLabelText(QFileDialog.Accept, 'import')
        if dialog.exec_():
            fname = dialog.selectedFiles()
        if type(fname) == list:
            path, name = os.path.split(fname[0])
            if fname[0]:
                shutil.copyfile(fname[0], self.materialPath + name)
        self.getComboBoxes()

    def addingCertificate(self):
        fname = ''
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setLabelText(QFileDialog.Accept, 'import')
        if dialog.exec_():
            fname = dialog.selectedFiles()
        if type(fname) == list:
            path, name = os.path.split(fname[0])
            if fname[0]:
                shutil.copyfile(fname[0], self.certificatePath + name)
        self.getComboBoxes()

    def disableEnableParticipantList(self, str):
        if str == 'begin':
            self.ui.addPart.setEnabled(False)
            self.ui.saveMat.setEnabled(False)

        if str == 'finished':
            self.ui.participants.setEnabled(True)
            self.ui.addPart.setEnabled(True)
            self.ui.saveMat.setEnabled(True)

    def disableEnableCertification(self, str):
        if str == 'begin':
            self.ui.locationCombo.setEnabled(False)
            self.ui.trainerCombo.setEnabled(False)
            self.ui.certCombo.setEnabled(False)
            self.ui.saveCert.setEnabled(False)

            self.ui.certDateTo.setEnabled(False)



        if str == 'finished':
            self.ui.locationCombo.setEnabled(True)
            self.ui.trainerCombo.setEnabled(True)
            self.ui.certCombo.setEnabled(True)
            self.ui.saveCert.setEnabled(True)

            self.ui.certDateTo.setEnabled(True)


    def progressingCertification(self,count):
        self.ui.progressBarCert.setValue(count)

    def progressingMaterial(self, count):
        self.ui.progressBarMat.setValue(count)

    def getParticipants(self):
        self.ui.participants.setEnabled(False)
        self.participantList = []
        for i in range(0, self.ui.participants.rowCount()):
            if self.ui.participants.item(i, 2):
                firstname = self.ui.participants.item(i, 0).text()
                lastname = self.ui.participants.item(i, 1).text()
                email = self.ui.participants.item(i, 2).text()
                self.participantList.append(Participant(firstname, lastname, email))

    def saveMaterialFiles(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory") + '/')
        temp = 'temp/mat/'
        onlyfiles = [f for f in listdir(temp) if isfile(join(temp, f))]
        for i in onlyfiles:
            shutil.move(temp + i, file + i)

    def saveCertificationFiles(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory") + '/')
        temp = 'temp/cert/'
        onlyfiles = [f for f in listdir(temp) if isfile(join(temp, f))]
        for i in onlyfiles:
            shutil.move(temp + i, file + i)


    def addCell(self):
        self.ui.participants.setEnabled(True)
        row = self.ui.participants.rowCount()
        self.ui.participants.insertRow(row)


class Participant():
    def __init__(self, firstname, lastname, email):
        self.firstname, self.lastname, self.email = firstname, lastname, email

    def __repr__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.email


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
            src = 'temp/mat/' + str(newfile) + '_' + str(participant.email) + '.pdf'
            outputStream = open(src, 'wb')
            output.write(outputStream)
            outputStream.close()
            # compress('output.pdf', 'temp/' + str(newfile) + '_' + str(participant.email) + '.pdf', power=0)
            #os.remove('output.pdf')

        self.finish.emit('finished')
        count = float(0)
        self.progress.emit(count)


class CWorker(QThread):
    progressCert = pyqtSignal(float)
    finish = pyqtSignal(str)

    def __init__(self, participants, date, location, path, filename, trainer):
        QThread.__init__(self)
        self.participants = participants
        self.date = date
        self.location = location
        self.path = path
        self.filename = filename
        self.trainer = trainer

    def run(self):
        self.finish.emit('begin')
        count = float(0)
        for participant in self.participants:
            generateCertificate(participant.firstname, participant.lastname, self.date, self.location, self.path,
                                self.filename, self.trainer)
            count += (float(100) / float(len(self.participants)))
        count = float(0)
        self.progressCert.emit(count)
        self.finish.emit('finished')
        # generateCertificate()


window = MainWindow()
window.show()

sys.exit(app.exec_())

# TODO
# adapt path for windows like in password manager
# read excel file
# open outlook
# closing programm not possible until data is saved somewhere
