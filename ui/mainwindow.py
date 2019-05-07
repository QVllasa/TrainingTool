# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 566)
        MainWindow.setMinimumSize(QtCore.QSize(626, 566))
        MainWindow.setMaximumSize(QtCore.QSize(626, 566))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 140, 611, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.materialTab = QtWidgets.QWidget()
        self.materialTab.setObjectName("materialTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.materialTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 581, 341))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBarMat = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.progressBarMat.setProperty("value", 0)
        self.progressBarMat.setObjectName("progressBarMat")
        self.gridLayout_2.addWidget(self.progressBarMat, 3, 0, 1, 4)
        self.saveMat = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.saveMat.setObjectName("saveMat")
        self.gridLayout_2.addWidget(self.saveMat, 2, 3, 1, 1)
        self.addWat = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.addWat.setObjectName("addWat")
        self.gridLayout_2.addWidget(self.addWat, 2, 2, 1, 1)
        self.participants = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.participants.setObjectName("participants")
        self.participants.setColumnCount(3)
        self.participants.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.participants.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.participants.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.participants.setHorizontalHeaderItem(2, item)
        self.participants.horizontalHeader().setVisible(True)
        self.participants.horizontalHeader().setCascadingSectionResizes(False)
        self.participants.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.participants, 0, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.addPart = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.addPart.setObjectName("addPart")
        self.gridLayout_2.addWidget(self.addPart, 2, 1, 1, 1)
        self.matCombo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.matCombo.setObjectName("matCombo")
        self.gridLayout_2.addWidget(self.matCombo, 1, 1, 1, 3)
        self.tabWidget.addTab(self.materialTab, "")
        self.certificateTab = QtWidgets.QWidget()
        self.certificateTab.setObjectName("certificateTab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.certificateTab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 591, 181))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.saveCert = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.saveCert.setObjectName("saveCert")
        self.gridLayout_3.addWidget(self.saveCert, 3, 3, 1, 1)
        self.certCombo = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.certCombo.setObjectName("certCombo")
        self.gridLayout_3.addWidget(self.certCombo, 3, 1, 1, 1)
        self.generateCert = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.generateCert.setObjectName("generateCert")
        self.gridLayout_3.addWidget(self.generateCert, 3, 2, 1, 1)
        self.progressBarCert = QtWidgets.QProgressBar(self.gridLayoutWidget_3)
        self.progressBarCert.setProperty("value", 24)
        self.progressBarCert.setObjectName("progressBarCert")
        self.gridLayout_3.addWidget(self.progressBarCert, 4, 0, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.locationText = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.locationText.setObjectName("locationText")
        self.gridLayout_3.addWidget(self.locationText, 1, 1, 1, 3)
        self.trainerText = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.trainerText.setObjectName("trainerText")
        self.gridLayout_3.addWidget(self.trainerText, 2, 1, 1, 3)
        self.certDate = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.certDate.setObjectName("certDate")
        self.gridLayout_3.addWidget(self.certDate, 0, 1, 1, 1)
        self.tabWidget.addTab(self.certificateTab, "")
        self.sendTab = QtWidgets.QWidget()
        self.sendTab.setObjectName("sendTab")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.sendTab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 10, 601, 341))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.openMail = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.openMail.setObjectName("openMail")
        self.gridLayout_4.addWidget(self.openMail, 2, 1, 1, 1)
        self.mailSubText = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.mailSubText.setObjectName("mailSubText")
        self.gridLayout_4.addWidget(self.mailSubText, 0, 1, 1, 1)
        self.mailText = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_4)
        self.mailText.setObjectName("mailText")
        self.gridLayout_4.addWidget(self.mailText, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.tabWidget.addTab(self.sendTab, "")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 601, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setEnabled(False)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MindSphere Academy Training Tool"))
        self.saveMat.setText(_translate("MainWindow", "Save "))
        self.addWat.setText(_translate("MainWindow", "Add Watermark"))
        item = self.participants.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Firstname"))
        item = self.participants.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lastname"))
        item = self.participants.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "E-Mail"))
        self.label_4.setText(_translate("MainWindow", "Select Material"))
        self.addPart.setText(_translate("MainWindow", "Add Participant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.materialTab), _translate("MainWindow", "1. Material Generator"))
        self.saveCert.setText(_translate("MainWindow", "Save"))
        self.generateCert.setText(_translate("MainWindow", "Generate Certificate"))
        self.label_9.setText(_translate("MainWindow", "Trainer"))
        self.label_5.setText(_translate("MainWindow", "Select Certificate"))
        self.label_8.setText(_translate("MainWindow", "Date"))
        self.label_10.setText(_translate("MainWindow", "Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.certificateTab), _translate("MainWindow", "2. Certificate Generator"))
        self.openMail.setText(_translate("MainWindow", "Open E-Mails"))
        self.label_6.setText(_translate("MainWindow", "Subject"))
        self.label_7.setText(_translate("MainWindow", "E-Mail Content"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sendTab), _translate("MainWindow", "3. Send"))
        self.label.setText(_translate("MainWindow", "Type in Training Date"))
        self.label_2.setText(_translate("MainWindow", "Choose Training"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Classroom"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "On-Site"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Webinar"))
        self.label_3.setText(_translate("MainWindow", "Type of Training"))


