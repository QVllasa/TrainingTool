# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\addTrainerDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrainerDialog(object):
    def setupUi(self, TrainerDialog):
        TrainerDialog.setObjectName("TrainerDialog")
        TrainerDialog.resize(400, 103)
        TrainerDialog.setMinimumSize(QtCore.QSize(400, 103))
        TrainerDialog.setMaximumSize(QtCore.QSize(400, 103))
        self.gridLayoutWidget = QtWidgets.QWidget(TrainerDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.trainerInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.trainerInput.setObjectName("trainerInput")
        self.gridLayout.addWidget(self.trainerInput, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Germany))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(TrainerDialog)
        self.buttonBox.accepted.connect(TrainerDialog.accept)
        self.buttonBox.rejected.connect(TrainerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TrainerDialog)

    def retranslateUi(self, TrainerDialog):
        _translate = QtCore.QCoreApplication.translate
        TrainerDialog.setWindowTitle(_translate("TrainerDialog", "Add Trainer"))


