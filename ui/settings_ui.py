# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Tue Nov  4 13:06:59 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(435, 287)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.generalTab = QtGui.QWidget()
        self.generalTab.setObjectName("generalTab")
        self.formLayout = QtGui.QFormLayout(self.generalTab)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.generalTab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.startupContext = QtGui.QComboBox(self.generalTab)
        self.startupContext.setObjectName("startupContext")
        self.startupContext.addItem("")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.startupContext)
        self.tabWidget.addTab(self.generalTab, "")
        self.notificationsTab = QtGui.QWidget()
        self.notificationsTab.setObjectName("notificationsTab")
        self.tabWidget.addTab(self.notificationsTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "workload settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Startup context", None, QtGui.QApplication.UnicodeUTF8))
        self.startupContext.setItemText(0, QtGui.QApplication.translate("Dialog", "Last opened", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab), QtGui.QApplication.translate("Dialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notificationsTab), QtGui.QApplication.translate("Dialog", "Notifications", None, QtGui.QApplication.UnicodeUTF8))

