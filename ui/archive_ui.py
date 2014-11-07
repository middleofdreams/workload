# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'archive.ui'
#
# Created: Fri Nov  7 11:01:07 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 462)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameFilter = QtGui.QLineEdit(Dialog)
        self.nameFilter.setObjectName("nameFilter")
        self.horizontalLayout.addWidget(self.nameFilter)
        self.contextFilter = QtGui.QLineEdit(Dialog)
        self.contextFilter.setObjectName("contextFilter")
        self.horizontalLayout.addWidget(self.contextFilter)
        self.createFilter = QtGui.QLineEdit(Dialog)
        self.createFilter.setObjectName("createFilter")
        self.horizontalLayout.addWidget(self.createFilter)
        self.closeFilter = QtGui.QLineEdit(Dialog)
        self.closeFilter.setObjectName("closeFilter")
        self.horizontalLayout.addWidget(self.closeFilter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(130)
        self.treeWidget.header().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.treeWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Workload - tasks archive", None, QtGui.QApplication.UnicodeUTF8))
        self.nameFilter.setPlaceholderText(QtGui.QApplication.translate("Dialog", "filter by task name", None, QtGui.QApplication.UnicodeUTF8))
        self.contextFilter.setPlaceholderText(QtGui.QApplication.translate("Dialog", "filter by context name", None, QtGui.QApplication.UnicodeUTF8))
        self.createFilter.setPlaceholderText(QtGui.QApplication.translate("Dialog", "filter by create date", None, QtGui.QApplication.UnicodeUTF8))
        self.closeFilter.setPlaceholderText(QtGui.QApplication.translate("Dialog", "filter by close date", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Dialog", "task name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("Dialog", "context", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("Dialog", "created", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(3, QtGui.QApplication.translate("Dialog", "closed", None, QtGui.QApplication.UnicodeUTF8))

