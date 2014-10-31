# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from ui.main_ui import Ui_MainWindow
from db import DB
from task import Task
import os


class Workload(QtGui.QMainWindow):

    def __init__(self,app):
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
        self.ui.taskList.activated.connect(self.openTask)
        sc = QtGui.QShortcut(self)
        sc.setKey("Escape")
        sc.activated.connect(self.closeEvent)
        
        self.ui.actionExit.triggered.connect(app.quit)
        
        self.ui.taskList.setColumnWidth(0, 20)
        self.currentContext = 1  # tymczasowo
        self.taskOpened=False
        
        self.db = DB(self)
        self.loadTasksList()
#CONNECT MENU ITEMS       
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionImport_tasklist.triggered.connect(self.importTasklist)
        self.ui.actionAbout_2.triggered.connect(self.about)
        self.ui.actionAdd_new.triggered.connect(self.createTask)
        self.ui.actionEdit.triggered.connect(self.openTask)
        self.ui.actionDelete.triggered.connect(self.deleteSelectedTasks)
        self.ui.actionComplete.triggered.connect(self.completeTasks)
        self.ui.actionHistory.triggered.connect(self.showHistory)
        self.ui.actionDefault.triggered.connect(self.manageContexts)
        self.ui.actionWork.triggered.connect(self.manageContexts)
        self.ui.actionHome.triggered.connect(self.manageContexts)
        self.ui.actionAdd_New_Context.triggered.connect(self.addContext)
        self.ui.actionRemove_Context.triggered.connect(self.removeContext)
        
        
        
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
                print(item.data(0,32))
        
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
        tasks=self.db.getTasks(self.currentContext)
        desiredHeight=22*len(tasks)+self.height()-self.ui.taskList.height()+2
        if ( desiredHeight>self.height() or downSize ) and desiredHeight<QtGui.QApplication.desktop().height():
            self.resize(self.width(),desiredHeight)
   
    def closeEvent(self, e=None):
        self.hide()
        if e:
            e.ignore()
                
###### MENU FUNCTIONS

    def importTasklist(self):
        dialog=QtGui.QFileDialog(self, "Open", "", "CSV File (*.csv)")
        if dialog.exec():
            filename=dialog.selectedFiles()
            print("ok, that's all, we have filename and now it needs to be opened and processed")
            print("idea is to import tasks from CSV file or something in more readable format")
            print("imported tasks will be placed under current context")
            print("import should contain priority;task name;due date;description")
               
    def about(self):
        print("some 'About' bullshit popup")
                  
    def exit(self):
        if self.questionPopup("Exit", "Are you sure?"):
            sys.exit()
        else:
            pass           
        
    def createTask(self):
        print("should open new empty dialog(same as for task edit) after OK, new task is created")

    def completeTasks(self):
        print("> take all selected task from list and change state to 'completed'")
        print("> all completed tasks should be removed from list, but kept in History")
    
    def showHistory(self):
        print("> gather all completed tasks and show in window with search feature")
        print("> when history entry is opened, normal task edit dialog is shown")
        print("> history is shown for all contexts")
    
    def manageContexts(self):
        print("> if one of existing contexts is checked, switch list and uncheck previous context")
        print("> contexts should be stored in list in order to manage them later")
        print("> maybe we should separate context management..")
    
    def addContext(self):
        print("> open input dialog where context name is entered")
        print("> create new item in menu and connects action(?) how simple is that...")
        print("> fuck it.. let's just support 10 contexts and only show used ones")
        print("> add new context information to context list")
        print("> names from list will be used as names in context menu")
        print("> if list entry is present, update context list")
    
    def removeContext(self):
        print("> open input dialog where context name is entered")
        print("> context is removed from context list")
        print("> update context list, items without label should be hidden")
      
    
  
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
    myapp = Workload(app)

    res = app.exec_()
    sys.exit()
