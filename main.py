# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from ui.main_ui import Ui_MainWindow
from db import DB
from task import Task
import os


class Workload(QtGui.QMainWindow):

    def __init__(self):
        '''main window init'''
        QtGui.QMainWindow.__init__(self)
        self.tray=Trayicon(self)   

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint
                            | QtCore.Qt.WindowStaysOnTopHint)

        desktop = QtGui.QApplication.desktop()
        if desktop.height() > 800:
            self.move(10, (desktop.height() / 2) - (self.height()))
        else:
            self.move(10, 10)

        self.show()

        self.ui.taskList.keyPressEvent = self.getKeysOnList
        self.ui.taskInput.keyPressEvent= self.getKeysOnInput
        #self.ui.taskList.itemSelectionChanged.connect(self.itemSelected)
        self.ui.taskList.activated.connect(self.openTask)
        
        sc = QtGui.QShortcut(self)
        sc.setKey("Escape")
        sc.activated.connect(self.closeEvent)
       
        self.ui.taskList.setColumnWidth(0, 20)
        self.currentContext = 1  # tymczasowo
        self.taskOpened=False
        
        self.db = DB(self)
        self.loadTasksList()
      
        
        
    # TASKS RELATED ACTIONS
    def addTask(self):
        t = self.ui.taskInput.text().strip()
        if t =="":
            return False
        self.ui.taskInput.clear()
        priority = 0
        try:
            if t[1] == ":":
                priority = int(t[0])
                if priority<6:
                    t = t[2:]
                else:
                    priority = 0

            elif t[-2] == ":":
                priority = int(t[-1])
                if priority<6:
                    t = t[:-2]
                else:
                    priority = 0
        except:
            pass
        taskid = self.db.addTask(t,priority,self.currentContext)
        self.createTaskItem(t, taskid, priority)
        self.adjustHeight()


    def createTaskItem(self, t, taskid=None, priority=0):
        item = QtGui.QTreeWidgetItem([str(priority), t])
        item.setData(0, 32, taskid) 
        item.setSizeHint(0, QtCore.QSize(0, 22))
        self.ui.taskList.addTopLevelItem(item)
        self.setPriorityColor(item, priority)
        self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)


    def loadTasksList(self, archived=False):
        for i in self.db.getTasks(self.currentContext):
            self.createTaskItem(i[1], i[0],i[2])
        self.adjustHeight()
            

    def deleteSelectedTasks(self, force=False):
        selectedItems = self.ui.taskList.selectedItems()
        if len(selectedItems)>0:
            tasks = []
            for item in selectedItems:
                tasks.append(item)
            if force:
                self.deleteTasks(tasks)
            elif self.questionPopup("Delete task",
                "Do you really want to delete selected  task(s) ?"):
                self.deleteTasks(tasks)
            self.adjustHeight(downSize=True)


    def deleteTasks(self, tasks):
        for item in tasks:
            self.db.deleteTask(item.data(0, 32))
            index = self.ui.taskList.indexOfTopLevelItem(item)
            self.ui.taskList.takeTopLevelItem(index)
        
        
    def setTaskPriority(self,priority):
        selectedItems = self.ui.taskList.selectedItems()
        for item in selectedItems:
            self.db.setTaskPriority(item.data(0, 32),priority)
            self.setPriorityColor(item, priority)
            item.setText(0,str(priority))
            self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)
                
    
    def setPriorityColor(self,item,priority):
        colors=["#98DCEB","#BD1515","#ED1B0C","#F2920C","#F2E63D","#8EDB84"]
        backColor = QtGui.QColor(colors[priority])  # kolor tła kolumny
        item.setBackground(0, backColor)     # (priorytet dla elementu)
        item.setTextAlignment(0,QtCore.Qt.AlignCenter)    
        
    def openTask(self):
        if not self.taskOpened:
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
            self.deleteSelectedTasks(force)
        elif e.key()>48 and e.key()<54:
            self.setTaskPriority(e.key()-48)    
        elif e.key()==16777221 or e.key()==16777220:  # enter/return
            self.openTask()
            
            
    def getKeysOnInput(self, e):
        print (e.key())
        if e.key()==16777221 or e.key()==16777220:  # enter/return
            self.addTask()
        else:
            QtGui.QLineEdit.keyPressEvent(self.ui.taskInput,e)


    #ADDITIONAL FUNTIONS
    def questionPopup(self, title, msg):
        resp = QtGui.QMessageBox.question(self, title, msg,
        buttons=QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        if resp == QtGui.QMessageBox.Ok:
            return True
        else:
            return False
        

        
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
        try:
            del(self.posx)
            del(self.posy)
        except:
            pass
        
    def adjustHeight(self,downSize=False):
        print(QtGui.QApplication.desktop().height())
        tasks=self.db.getTasks(self.currentContext)
        desiredHeight=22*len(tasks)+self.height()-self.ui.taskList.height()+2
        if ( desiredHeight>self.height() or downSize ) and desiredHeight<QtGui.QApplication.desktop().height():
            self.resize(self.x(),desiredHeight)
            
            
    def closeEvent(self, e=None):
        self.hide()
        if e:
            e.ignore()
  
class Trayicon(QtGui.QSystemTrayIcon):
    def __init__(self,parent=None):
        QtGui.QSystemTrayIcon.__init__(self,parent)
        self.parent=parent
        icon=QtGui.QIcon(os.path.realpath("icon.png"))
        self.setIcon(icon)
        self.show()
        self.activated.connect(self.showApp)
    def showApp(self):
        if self.parent.isVisible():
            self.parent.hide()
        else:
            self.parent.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = Workload()

    res = app.exec_()
    sys.exit()
