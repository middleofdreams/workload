# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ui.main_ui import Ui_MainWindow
from db import DB


class Workload(QtGui.QMainWindow):

    def __init__(self):
        '''main window init'''
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint
                            | QtCore.Qt.WindowStaysOnTopHint)

        desktop = QtGui.QApplication.desktop()

        self.move(10, (desktop.height() / 2) - (self.height()))

        self.show()

        self.ui.taskList.keyReleaseEvent = self.getKeysOnList
        k = QtGui.QShortcut(self)
        k.setKey("Return")
        k.activated.connect(self.addTask)
        k = QtGui.QShortcut(self)
        k.setKey("Enter")
        k.activated.connect(self.addTask)
        self.ui.taskList.setColumnWidth(0, 20)
        self.currentContext = 1  # tymczasowo

        self.db = DB(self)
        self.loadTasksList()

    # TASKS RELATED ACTIONS
    def addTask(self):
        t = self.ui.taskInput.text().strip()
        self.ui.taskInput.clear()
        priority = 0
        try:
            if t[1] == ":":
                priority = int(t[0])
                t = t[2:]

            elif t[-2] == ":":
                priority = int(t[-1])
                t = t[:-3]
        except:
            pass

        taskid = self.db.addTask(t)
        self.createTaskItem(t, taskid, priority)

    def createTaskItem(self, t, taskid=None, priority=0):
        print(priority)
        item = QtGui.QTreeWidgetItem(["", t])
        item.setData(0, 32, taskid)
        item.setSizeHint(0, QtCore.QSize(0, 22))
        self.ui.taskList.addTopLevelItem(item)

        backColor = QtGui.QColor("#ff0000")  # kolor tła kolumny
        item.setBackground(0, backColor)     # (priorytet dla elementu)

    def loadTasksList(self, archived=False):
        for i in self.db.getTasks(self.currentContext):
            self.createTaskItem(i[1], i[0])

    def deleteSelectedTask(self, force=False):
        selectedItems = self.ui.taskList.selectedItems()
        if len(selectedItems) > 0:
            item = self.ui.taskList.selectedItems()[0]
            if force:
                self.deleteTask(item)
            elif self.questionPopup("Delete task",
                "Do you really want to delete task " + item.text(1) + "?"):
                self.deleteTask(item)

    def deleteTask(self, item):
            self.db.deleteTask(item.data(0, 32))
            index = self.ui.taskList.indexOfTopLevelItem(item)
            self.ui.taskList.takeTopLevelItem(index)

    # SHORTCUTS AND KEYBOARD EVENTS RELATED ACTIONS
    def getKeysOnList(self, e):
        print((e.key()))
        if e.key() == 16777223:  # delete
            force = False
            if (QtCore.Qt.ShiftModifier & e.modifiers()):
                force = True
            self.deleteSelectedTask(force)

    #ADDITIONAL FUNTIONS
    def questionPopup(self, title, msg):
        resp = QtGui.QMessageBox.question(self, title, msg,
        buttons=QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        if resp == QtGui.QMessageBox.Ok:
            return True
        else:
            return False

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = Workload()

    res = app.exec_()
    sys.exit()
