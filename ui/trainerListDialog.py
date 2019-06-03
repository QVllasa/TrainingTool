# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\trainerListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RemoveTrainerDialog(object):
    def setupUi(self, RemoveTrainerDialog):
        RemoveTrainerDialog.setObjectName("RemoveTrainerDialog")
        RemoveTrainerDialog.resize(400, 300)
        self.trainerList = QtWidgets.QTableWidget(RemoveTrainerDialog)
        self.trainerList.setGeometry(QtCore.QRect(20, 20, 256, 261))
        self.trainerList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.trainerList.setObjectName("trainerList")
        self.trainerList.setColumnCount(1)
        self.trainerList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.trainerList.setHorizontalHeaderItem(0, item)
        self.trainerList.horizontalHeader().setVisible(False)
        self.trainerList.horizontalHeader().setStretchLastSection(True)
        self.removeButton = QtWidgets.QPushButton(RemoveTrainerDialog)
        self.removeButton.setGeometry(QtCore.QRect(280, 20, 113, 32))
        self.removeButton.setObjectName("removeButton")
        self.cancelButton = QtWidgets.QPushButton(RemoveTrainerDialog)
        self.cancelButton.setGeometry(QtCore.QRect(280, 60, 113, 32))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(RemoveTrainerDialog)
        QtCore.QMetaObject.connectSlotsByName(RemoveTrainerDialog)

    def retranslateUi(self, RemoveTrainerDialog):
        _translate = QtCore.QCoreApplication.translate
        RemoveTrainerDialog.setWindowTitle(_translate("RemoveTrainerDialog", "Trainer List"))
        item = self.trainerList.horizontalHeaderItem(0)
        item.setText(_translate("RemoveTrainerDialog", "Neue Spalte"))
        self.removeButton.setText(_translate("RemoveTrainerDialog", "Remove"))
        self.cancelButton.setText(_translate("RemoveTrainerDialog", "Cancel"))


