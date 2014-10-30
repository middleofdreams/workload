# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ui.main_ui import Ui_MainWindow
from db import DB
from task import Task


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
        self.ui.taskInput.keyReleaseEvent= self.getKeysOnInput
        self.ui.taskList.keyPressEvent=self.dummy
       
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
                t = t[:-2]
        except:
            pass
        taskid = self.db.addTask(t,priority,self.currentContext)
        self.createTaskItem(t, taskid, priority)

    def createTaskItem(self, t, taskid=None, priority=0):
        item = QtGui.QTreeWidgetItem([str(priority), t])
        item.setData(0, 32, taskid) 
        item.setSizeHint(0, QtCore.QSize(0, 22))
        self.ui.taskList.addTopLevelItem(item)
        # TODO: kolorki do priorytetow
        self.setPriorityColor(item, priority)
        self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)

    def loadTasksList(self, archived=False):
        for i in self.db.getTasks(self.currentContext):
            self.createTaskItem(i[1], i[0],i[2])

    def deleteSelectedTask(self, force=False):
        item = self.getSelectedItem()
        if item:
            if force:
                self.deleteTask(item)
            elif self.questionPopup("Delete task",
                "Do you really want to delete task " + item.text(1) + "?"):
                self.deleteTask(item)

    def deleteTask(self, item):
        self.db.deleteTask(item.data(0, 32))
        index = self.ui.taskList.indexOfTopLevelItem(item)
        self.ui.taskList.takeTopLevelItem(index)
        
    def setTaskPriority(self,priority):
        item = self.getSelectedItem()
        if item:
            self.db.setTaskPriority(item.data(0, 32),priority)
            self.setPriorityColor(item, priority)
            item.setText(0,str(priority))
            self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)
            
            # TODO: zmienic priority w itemie - Jasiu do boju!
    
    def setPriorityColor(self,item,priority):
        colors=["#98DCEB","#F21835","#F56056","#FFC582","#FC7168","#8EDB84"]
        backColor = QtGui.QColor(colors[priority])  # kolor tła kolumny
        item.setBackground(0, backColor)     # (priorytet dla elementu)
        
    def openTask(self):
        item = self.getSelectedItem()
        if item:
            Task(self,item.data(0, 32))
        
    def getSelectedItem(self):
        selectedItems = self.ui.taskList.selectedItems()
        if len(selectedItems) > 0:
            item = self.ui.taskList.selectedItems()[0]
            return item
        else:
            return False

    # SHORTCUTS AND KEYBOARD EVENTS RELATED ACTIONS
    def getKeysOnList(self, e):
        if e.key() == 16777223:  # delete
            force = False
            if (QtCore.Qt.ShiftModifier & e.modifiers()):
                force = True
            self.deleteSelectedTask(force)
        elif e.key()>48 and e.key()<54:
            self.setTaskPriority(e.key()-48)    
        elif e.key()==16777221 or e.key()==16777220:  # enter/return
            self.openTask()
            
    def getKeysOnInput(self, e):
        if e.key()==16777221 or e.key()==16777220:  # enter/return
            self.addTask()

    #ADDITIONAL FUNTIONS
    def questionPopup(self, title, msg):
        resp = QtGui.QMessageBox.question(self, title, msg,
        buttons=QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        if resp == QtGui.QMessageBox.Ok:
            return True
        else:
            return False
        
    def dummy(self,*args):
        pass

    #WINDOWS MOVEMENT
    def mouseMoveEvent(self, e):
        try:
            self.posx
            self.posy
        except:
            self.posx=e.x()
            self.posy=e.y()
        y=e.globalY()-self.posy
        x=e.globalX()-self.posx
     
        self.move(x,y)

    def mouseReleaseEvent(self, e):
        del(self.posx)
        del(self.posy)
            

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = Workload()

    res = app.exec_()
    sys.exit()
