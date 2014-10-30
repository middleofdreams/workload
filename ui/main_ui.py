# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workspace/Workload/src-raw/ui/main.ui'
#
# Created: Wed Oct 29 22:05:56 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(190, 320)
        MainWindow.setMinimumSize(QtCore.QSize(190, 320))
        MainWindow.setMaximumSize(QtCore.QSize(300, 600))
        MainWindow.setWindowOpacity(0.9)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.taskInput = QtGui.QLineEdit(self.centralwidget)
        self.taskInput.setObjectName("taskInput")
        self.verticalLayout.addWidget(self.taskInput)
        self.taskList = QtGui.QTreeWidget(self.centralwidget)
        self.taskList.setEnabled(True)
        self.taskList.setBaseSize(QtCore.QSize(0, 0))
        self.taskList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.taskList.setTextElideMode(QtCore.Qt.ElideLeft)
        self.taskList.setAutoExpandDelay(-1)
        self.taskList.setIndentation(0)
        self.taskList.setRootIsDecorated(False)
        self.taskList.setColumnCount(2)
        self.taskList.setObjectName("taskList")
        self.taskList.header().setVisible(False)
        self.taskList.header().setDefaultSectionSize(20)
        self.taskList.header().setMinimumSectionSize(10)
        self.verticalLayout.addWidget(self.taskList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 190, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTask = QtGui.QMenu(self.menubar)
        self.menuTask.setObjectName("menuTask")
        self.menuContext = QtGui.QMenu(self.menubar)
        self.menuContext.setObjectName("menuContext")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDefault = QtGui.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.menuFile.addAction(self.actionExit)
        self.menuContext.addAction(self.actionDefault)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTask.menuAction())
        self.menubar.addAction(self.menuContext.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Workload", None, QtGui.QApplication.UnicodeUTF8))
        self.taskList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.taskList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Task", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTask.setTitle(QtGui.QApplication.translate("MainWindow", "Task", None, QtGui.QApplication.UnicodeUTF8))
        self.menuContext.setTitle(QtGui.QApplication.translate("MainWindow", "Context", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDefault.setText(QtGui.QApplication.translate("MainWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))

