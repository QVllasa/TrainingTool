# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 583)
        MainWindow.setMinimumSize(QtCore.QSize(719, 583))
        MainWindow.setMaximumSize(QtCore.QSize(719, 583))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 140, 681, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.materialTab = QtWidgets.QWidget()
        self.materialTab.setObjectName("materialTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.materialTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 661, 341))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addMaterial = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.addMaterial.setObjectName("addMaterial")
        self.gridLayout_2.addWidget(self.addMaterial, 2, 0, 1, 1)
        self.addPart = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.addPart.setObjectName("addPart")
        self.gridLayout_2.addWidget(self.addPart, 2, 1, 1, 1)
        self.participants = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.participants.setEnabled(True)
        self.participants.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.participants.setObjectName("participants")
        self.participants.setColumnCount(3)
        self.participants.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.participants.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.participants.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.participants.setHorizontalHeaderItem(2, item)
        self.participants.horizontalHeader().setVisible(False)
        self.participants.horizontalHeader().setCascadingSectionResizes(False)
        self.participants.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.participants, 0, 0, 1, 6)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.matCombo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.matCombo.setObjectName("matCombo")
        self.gridLayout_2.addWidget(self.matCombo, 1, 1, 1, 4)
        self.saveMat = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.saveMat.setObjectName("saveMat")
        self.gridLayout_2.addWidget(self.saveMat, 2, 4, 1, 1)
        self.addWat = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.addWat.setObjectName("addWat")
        self.gridLayout_2.addWidget(self.addWat, 2, 3, 1, 1)
        self.progressBarMat = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
        self.progressBarMat.setProperty("value", 0)
        self.progressBarMat.setObjectName("progressBarMat")
        self.gridLayout_2.addWidget(self.progressBarMat, 3, 0, 1, 6)
        self.tabWidget.addTab(self.materialTab, "")
        self.certificateTab = QtWidgets.QWidget()
        self.certificateTab.setObjectName("certificateTab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.certificateTab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 661, 364))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.removeTrainer = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.removeTrainer.setObjectName("removeTrainer")
        self.gridLayout_3.addWidget(self.removeTrainer, 14, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.checkBoxFrom = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBoxFrom.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxFrom.setChecked(True)
        self.checkBoxFrom.setObjectName("checkBoxFrom")
        self.horizontalLayout.addWidget(self.checkBoxFrom)
        self.certDateFrom = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.certDateFrom.setCalendarPopup(True)
        self.certDateFrom.setDate(QtCore.QDate(2019, 5, 1))
        self.certDateFrom.setObjectName("certDateFrom")
        self.horizontalLayout.addWidget(self.certDateFrom)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.certDateTo = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
        self.certDateTo.setCalendarPopup(True)
        self.certDateTo.setDate(QtCore.QDate(2019, 5, 1))
        self.certDateTo.setObjectName("certDateTo")
        self.horizontalLayout.addWidget(self.certDateTo)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 2, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 4, 2, 1, 5)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 2, 1, 1)
        self.generateCert = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generateCert.setFont(font)
        self.generateCert.setObjectName("generateCert")
        self.gridLayout_3.addWidget(self.generateCert, 5, 6, 1, 1)
        self.saveCert = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.saveCert.setObjectName("saveCert")
        self.gridLayout_3.addWidget(self.saveCert, 6, 6, 1, 1)
        self.addTrainer = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.addTrainer.setObjectName("addTrainer")
        self.gridLayout_3.addWidget(self.addTrainer, 13, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 2, 1, 1)
        self.progressBarCert = QtWidgets.QProgressBar(self.gridLayoutWidget_3)
        self.progressBarCert.setProperty("value", 0)
        self.progressBarCert.setObjectName("progressBarCert")
        self.gridLayout_3.addWidget(self.progressBarCert, 5, 2, 1, 4)
        self.checkBoxLocation = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBoxLocation.setObjectName("checkBoxLocation")
        self.gridLayout_3.addWidget(self.checkBoxLocation, 1, 2, 1, 1)
        self.certCombo = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.certCombo.setObjectName("certCombo")
        self.gridLayout_3.addWidget(self.certCombo, 3, 3, 1, 4)
        self.trainerCombo = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.trainerCombo.setObjectName("trainerCombo")
        self.gridLayout_3.addWidget(self.trainerCombo, 2, 3, 1, 4)
        self.locationCombo = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.locationCombo.setObjectName("locationCombo")
        self.gridLayout_3.addWidget(self.locationCombo, 1, 3, 1, 4)
        self.addCertificate = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.addCertificate.setObjectName("addCertificate")
        self.gridLayout_3.addWidget(self.addCertificate, 9, 2, 1, 2)
        self.addLocation = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.addLocation.setObjectName("addLocation")
        self.gridLayout_3.addWidget(self.addLocation, 13, 3, 1, 1)
        self.removeLocation = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.removeLocation.setObjectName("removeLocation")
        self.gridLayout_3.addWidget(self.removeLocation, 14, 3, 1, 1)
        self.tabWidget.addTab(self.certificateTab, "")
        self.sendTab = QtWidgets.QWidget()
        self.sendTab.setObjectName("sendTab")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.sendTab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(0, 10, 671, 341))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 1, 2, 1, 1)
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
        self.openMail = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.openMail.setObjectName("openMail")
        self.gridLayout_4.addWidget(self.openMail, 2, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)
        self.mailSubText = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.mailSubText.setObjectName("mailSubText")
        self.gridLayout_4.addWidget(self.mailSubText, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_4.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.tabWidget.addTab(self.sendTab, "")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 691, 130))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.trainingType = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.trainingType.setObjectName("trainingType")
        self.trainingType.addItem("")
        self.trainingType.addItem("")
        self.trainingType.addItem("")
        self.gridLayout.addWidget(self.trainingType, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.trainingCourseCombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.trainingCourseCombo.setEnabled(True)
        self.trainingCourseCombo.setObjectName("trainingCourseCombo")
        self.gridLayout.addWidget(self.trainingCourseCombo, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.openData = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openData.setObjectName("openData")
        self.gridLayout.addWidget(self.openData, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.trainingStartCombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.trainingStartCombo.setObjectName("trainingStartCombo")
        self.gridLayout.addWidget(self.trainingStartCombo, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.checkBoxFrom.toggled['bool'].connect(self.certDateFrom.setEnabled)
        self.checkBoxLocation.toggled['bool'].connect(self.locationCombo.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MindSphere Academy Training Tool"))
        self.addMaterial.setText(_translate("MainWindow", "Import Material"))
        self.addPart.setText(_translate("MainWindow", "Add Participant"))
        item = self.participants.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Firstname"))
        item = self.participants.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lastname"))
        item = self.participants.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "E-Mail"))
        self.label_4.setText(_translate("MainWindow", "Select Material:"))
        self.saveMat.setText(_translate("MainWindow", "Save "))
        self.addWat.setText(_translate("MainWindow", "Add Watermark"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.materialTab), _translate("MainWindow", "1. Material Generator"))
        self.removeTrainer.setText(_translate("MainWindow", "Remove Trainer"))
        self.label_8.setText(_translate("MainWindow", "Date"))
        self.checkBoxFrom.setText(_translate("MainWindow", "from"))
        self.certDateFrom.setDisplayFormat(_translate("MainWindow", "dd"))
        self.label_11.setText(_translate("MainWindow", "to"))
        self.certDateTo.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_9.setText(_translate("MainWindow", "Trainer"))
        self.generateCert.setText(_translate("MainWindow", "Generate Certificate"))
        self.saveCert.setText(_translate("MainWindow", "Save"))
        self.addTrainer.setText(_translate("MainWindow", "Add Trainer"))
        self.label_5.setText(_translate("MainWindow", "Select Certificate"))
        self.checkBoxLocation.setText(_translate("MainWindow", "Location"))
        self.addCertificate.setText(_translate("MainWindow", "Import Certificate"))
        self.addLocation.setText(_translate("MainWindow", "Add Location"))
        self.removeLocation.setText(_translate("MainWindow", "Remove Location"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.certificateTab), _translate("MainWindow", "2. Certificate Generator"))
        self.label_6.setText(_translate("MainWindow", "Subject:"))
        self.label_7.setText(_translate("MainWindow", "E-Mail Content:"))
        self.openMail.setText(_translate("MainWindow", "Open Outlook"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MindConnect"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Development"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Introduction"))
        self.label_12.setText(_translate("MainWindow", "E-Mail Templates:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sendTab), _translate("MainWindow", "3. Send"))
        self.trainingType.setItemText(0, _translate("MainWindow", "Classroom"))
        self.trainingType.setItemText(1, _translate("MainWindow", "On-Site"))
        self.trainingType.setItemText(2, _translate("MainWindow", "Webinar"))
        self.label_3.setText(_translate("MainWindow", "Type of Training"))
        self.label.setText(_translate("MainWindow", "Filter Training Date"))
        self.label_2.setText(_translate("MainWindow", "Choose Training"))
        self.openData.setText(_translate("MainWindow", "Open"))
        self.label_13.setText(_translate("MainWindow", "Participant List:"))


