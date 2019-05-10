# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/LocationListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RemoveLocationDialog(object):
    def setupUi(self, RemoveLocationDialog):
        RemoveLocationDialog.setObjectName("RemoveLocationDialog")
        RemoveLocationDialog.resize(400, 300)
        self.locationList = QtWidgets.QTableWidget(RemoveLocationDialog)
        self.locationList.setGeometry(QtCore.QRect(20, 20, 256, 261))
        self.locationList.setObjectName("locationList")
        self.locationList.setColumnCount(1)
        self.locationList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.locationList.setHorizontalHeaderItem(0, item)
        self.locationList.horizontalHeader().setVisible(False)
        self.locationList.horizontalHeader().setStretchLastSection(True)
        self.locationList.verticalHeader().setVisible(True)
        self.removeButton = QtWidgets.QPushButton(RemoveLocationDialog)
        self.removeButton.setGeometry(QtCore.QRect(280, 20, 113, 32))
        self.removeButton.setObjectName("removeButton")
        self.cancelButton = QtWidgets.QPushButton(RemoveLocationDialog)
        self.cancelButton.setGeometry(QtCore.QRect(280, 60, 113, 32))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(RemoveLocationDialog)
        QtCore.QMetaObject.connectSlotsByName(RemoveLocationDialog)

    def retranslateUi(self, RemoveLocationDialog):
        _translate = QtCore.QCoreApplication.translate
        RemoveLocationDialog.setWindowTitle(_translate("RemoveLocationDialog", "Location List"))
        self.removeButton.setText(_translate("RemoveLocationDialog", "Remove"))
        self.cancelButton.setText(_translate("RemoveLocationDialog", "Cancel"))


