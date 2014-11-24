# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Nov 22 18:45:23 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(190, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(190, 320))
        MainWindow.setMaximumSize(QtCore.QSize(300, 600))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.9)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.taskInput = QtGui.QLineEdit(self.centralwidget)
        self.taskInput.setObjectName("taskInput")
        self.verticalLayout.addWidget(self.taskInput)
        self.taskList = QtGui.QTreeWidget(self.centralwidget)
        self.taskList.setEnabled(True)
        self.taskList.setBaseSize(QtCore.QSize(0, 0))
        self.taskList.setAcceptDrops(True)
        self.taskList.setAutoFillBackground(True)
        self.taskList.setFrameShape(QtGui.QFrame.Panel)
        self.taskList.setFrameShadow(QtGui.QFrame.Plain)
        self.taskList.setLineWidth(1)
        self.taskList.setMidLineWidth(1)
        self.taskList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.taskList.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.taskList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.taskList.setAlternatingRowColors(True)
        self.taskList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.taskList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.taskList.setTextElideMode(QtCore.Qt.ElideRight)
        self.taskList.setAutoExpandDelay(-1)
        self.taskList.setIndentation(10)
        self.taskList.setRootIsDecorated(False)
        self.taskList.setUniformRowHeights(False)
        self.taskList.setAnimated(True)
        self.taskList.setHeaderHidden(True)
        self.taskList.setColumnCount(3)
        self.taskList.setObjectName("taskList")
        self.taskList.header().setVisible(False)
        self.taskList.header().setCascadingSectionResizes(False)
        self.taskList.header().setDefaultSectionSize(5)
        self.taskList.header().setHighlightSections(False)
        self.taskList.header().setMinimumSectionSize(5)
        self.taskList.header().setSortIndicatorShown(False)
        self.taskList.header().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.taskList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 190, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTask = QtGui.QMenu(self.menubar)
        self.menuTask.setObjectName("menuTask")
        self.menuContext = QtGui.QMenu(self.menubar)
        self.menuContext.setObjectName("menuContext")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setMenuRole(QtGui.QAction.NoRole)
        self.actionExit.setObjectName("actionExit")
        self.actionDefault = QtGui.QAction(MainWindow)
        self.actionDefault.setCheckable(True)
        self.actionDefault.setObjectName("actionDefault")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionImport_tasklist = QtGui.QAction(MainWindow)
        self.actionImport_tasklist.setObjectName("actionImport_tasklist")
        self.actionAdd_new = QtGui.QAction(MainWindow)
        self.actionAdd_new.setObjectName("actionAdd_new")
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionComplete = QtGui.QAction(MainWindow)
        self.actionComplete.setObjectName("actionComplete")
        self.actionHistory = QtGui.QAction(MainWindow)
        self.actionHistory.setObjectName("actionHistory")
        self.actionEdit = QtGui.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionWork = QtGui.QAction(MainWindow)
        self.actionWork.setCheckable(True)
        self.actionWork.setObjectName("actionWork")
        self.actionHome = QtGui.QAction(MainWindow)
        self.actionHome.setCheckable(True)
        self.actionHome.setObjectName("actionHome")
        self.actionAdd_New_Context = QtGui.QAction(MainWindow)
        self.actionAdd_New_Context.setObjectName("actionAdd_New_Context")
        self.actionAbout_2 = QtGui.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionRemove_Context = QtGui.QAction(MainWindow)
        self.actionRemove_Context.setObjectName("actionRemove_Context")
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExport_tasklist = QtGui.QAction(MainWindow)
        self.actionExport_tasklist.setObjectName("actionExport_tasklist")
        self.menuFile.addAction(self.actionImport_tasklist)
        self.menuFile.addAction(self.actionExport_tasklist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionAbout_2)
        self.menuFile.addAction(self.actionExit)
        self.menuTask.addAction(self.actionAdd_new)
        self.menuTask.addAction(self.actionEdit)
        self.menuTask.addAction(self.actionComplete)
        self.menuTask.addAction(self.actionDelete)
        self.menuTask.addSeparator()
        self.menuTask.addAction(self.actionHistory)
        self.menuContext.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTask.menuAction())
        self.menubar.addAction(self.menuContext.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Workload", None, QtGui.QApplication.UnicodeUTF8))
        self.taskList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.taskList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "priority_icon", None, QtGui.QApplication.UnicodeUTF8))
        self.taskList.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Task", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTask.setTitle(QtGui.QApplication.translate("MainWindow", "&Task", None, QtGui.QApplication.UnicodeUTF8))
        self.menuContext.setTitle(QtGui.QApplication.translate("MainWindow", "&Context", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDefault.setText(QtGui.QApplication.translate("MainWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_tasklist.setText(QtGui.QApplication.translate("MainWindow", "&Import tasklist", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_tasklist.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_new.setText(QtGui.QApplication.translate("MainWindow", "&Add new", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_new.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionComplete.setText(QtGui.QApplication.translate("MainWindow", "&Complete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionComplete.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Return", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory.setText(QtGui.QApplication.translate("MainWindow", "&History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit.setText(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWork.setText(QtGui.QApplication.translate("MainWindow", "Work", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setText(QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_New_Context.setText(QtGui.QApplication.translate("MainWindow", "Add New Context", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_New_Context.setToolTip(QtGui.QApplication.translate("MainWindow", "&Add New Context", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_New_Context.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_2.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_2.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_Context.setText(QtGui.QApplication.translate("MainWindow", "Remove Context", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_Context.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Alt+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_tasklist.setText(QtGui.QApplication.translate("MainWindow", "&Export tasklist", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_tasklist.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+E", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
