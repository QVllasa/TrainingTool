# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/addLocationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LocationDialog(object):
    def setupUi(self, LocationDialog):
        LocationDialog.setObjectName("LocationDialog")
        LocationDialog.resize(400, 103)
        LocationDialog.setMinimumSize(QtCore.QSize(400, 103))
        LocationDialog.setMaximumSize(QtCore.QSize(400, 103))
        self.gridLayoutWidget = QtWidgets.QWidget(LocationDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.locationInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.locationInput.setObjectName("locationInput")
        self.gridLayout.addWidget(self.locationInput, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Germany))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(LocationDialog)
        self.buttonBox.accepted.connect(LocationDialog.accept)
        self.buttonBox.rejected.connect(LocationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LocationDialog)

    def retranslateUi(self, LocationDialog):
        _translate = QtCore.QCoreApplication.translate
        LocationDialog.setWindowTitle(_translate("LocationDialog", "Add  Location"))


