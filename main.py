# -*- coding: utf-8 -*-
from PySide import QtGui,QtCore
from ui.main_ui import Ui_MainWindow
from db import DB
from task import Task
from tray import Trayicon
import os,sys

class Workload(QtGui.QMainWindow):

    def __init__(self,app):
        '''main window init'''
        QtGui.QMainWindow.__init__(self)
        self.tray=Trayicon(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #GUI setting
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint
                            | QtCore.Qt.WindowStaysOnTopHint)
        desktop = QtGui.QApplication.desktop()
        if desktop.height() > 800:
            self.move(10, (desktop.height() / 2) - (self.height()))
        else:
            self.move(10, 10)
        self.ui.taskList.setColumnWidth(0, 20)

#CONNECT SIGNALS
        self.ui.taskList.keyPressEvent = self.getKeysOnList
        self.ui.taskInput.keyPressEvent= self.getKeysOnInput
        self.ui.taskList.activated.connect(self.openTask)
        sc = QtGui.QShortcut(self)
        sc.setKey("Escape")
        sc.activated.connect(self.closeEvent)
        
        sc = QtGui.QShortcut(self)
        sc.setKey("Ctrl+R")
        sc.activated.connect(self.adjustHeight)

#CONNECT MENU ITEMS
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionImport_tasklist.triggered.connect(self.importTasklist)
        self.ui.actionAbout_2.triggered.connect(self.about)
        self.ui.actionAdd_new.triggered.connect(self.createTask)
        self.ui.actionEdit.triggered.connect(self.openTask)
        self.ui.actionDelete.triggered.connect(self.deleteSelectedTasks)
        self.ui.actionComplete.triggered.connect(self.completeTasks)
        self.ui.actionHistory.triggered.connect(self.showHistory)
        self.ui.taskInput.dropEvent = self.dropTask
        
# SET VARIABLES AND CONNECT TO DB:

        self.currentContext = 1  # TODO: read contexts from db, set current one, fill menu
        self.taskOpened = False
        self.app = app
        self.db = DB(self)
        self.show()

        self.loadTasksList(init=True)
        self.loadContexts()

#finally - show the window:
        
    def dropTask(self,e):
        fulldata=e.mimeData().text()
        if len(fulldata) > 20:
            newdata=[]
            textFound=False
            for i in fulldata.splitlines():
                if i.strip()!="" or textFound: 
                    newdata.append(i)
                    textFound=True
            newdata="\n".join(newdata)
            taskname=newdata[:17].strip()+"..."
            taskDescription=newdata
            self.ui.taskInput.setText(taskname)
            self.addTask(taskDescription)
        #self.ui.taskInput.setText()

# TASKS RELATED ACTIONS
    def addTask(self,taskDescription):
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
#TODO: create new function to handle input (regexp etc)
        duedate=None
        taskid = self.db.addTask(t,priority, taskDescription, duedate, self.currentContext)
        self.createTaskItem(t, taskid, priority)
        self.adjustHeight()

    def createTaskItem(self, t, taskid=None, priority=0):
        item = QtGui.QTreeWidgetItem([str(priority), t])
        item.setData(0, 32, taskid)
        item.setSizeHint(0, QtCore.QSize(0, 22))
        self.ui.taskList.addTopLevelItem(item)
        self.setPriorityColor(item, priority)
        self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)


    def loadTasksList(self, archived=False,init=False):
        self.ui.taskList.clear()
        for i in self.db.getTasks(self.currentContext):
            self.createTaskItem(i[1], i[0],i[2])
        self.adjustHeight(init=init)


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
                #print(item.data(0,32))

    def getSelectedItem(self):
        selectedItems = self.ui.taskList.selectedItems()
        if len(selectedItems) == 1:
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
            if(QtCore.Qt.ControlModifier & e.modifiers()):
                self.completeTasks()
            else:
                self.openTask()


    def getKeysOnInput(self, e):
       # print (e.key())
        if e.key()==16777221 or e.key()==16777220:  # enter/return
            self.addTask(taskDescription=None)
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

    def adjustHeight(self,downSize=False,init=False):
        tasks=self.db.getTasks(self.currentContext)
        print(len(tasks))
        if init:
            winheight=320
            listheight=252
        else:
            winheight=self.height()
            listheight=self.ui.taskList.height()
        desiredHeight=22*len(tasks)+winheight-listheight+2
        if ( desiredHeight>self.height() or downSize ) and desiredHeight<QtGui.QApplication.desktop().height():
            self.resize(self.width(),desiredHeight)

    def closeEvent(self, e=None):
        self.hide()
        if e:
            e.ignore()

###### MENU FUNCTIONS

    def importTasklist(self):
        dialog=QtGui.QFileDialog(self, "Open", "", "CSV File (*.csv)")
        if dialog.exec_():
            filename=dialog.selectedFiles()
            #TODO: function for importing csv's
            print("ok, that's all, we have filename and now it needs to be opened and processed")
            print("idea is to import tasks from CSV file or something in more readable format")
            print("imported tasks will be placed under current context")
            print("import should contain priority;task name;due date;description")

    def about(self):
        f=open("about")
        text=f.read()
        f.close()
        about = QtGui.QMessageBox.information(self, "About", text,
        buttons=QtGui.QMessageBox.Ok )
        print("some 'About' bullshit popup")

    def exit(self):
        if self.questionPopup("Exit", "Are you sure?"):
            self.app.exit()  # cleaner than sys.exit allows Qt loop to end

    def createTask(self):
        Task(self,taskid=0)

    def completeTasks(self):
        tasks=self.ui.taskList.selectedItems()
        for i in tasks:
            self.db.completeTask(i.data(0,32))
            index = self.ui.taskList.indexOfTopLevelItem(i)
            self.ui.taskList.takeTopLevelItem(index)

    def showHistory(self):
        #TODO: Create new window, similar to main one with search instead of input
        print("> gather all completed tasks and show in window with search feature")
        print("> when history entry is opened, normal task edit dialog is shown")
        print("> history is shown for all contexts")

    def manageContexts(self):
        #TODO: context management
        print("> if one of existing contexts is checked, switch list and uncheck previous context")
        print("> contexts should be stored in list in order to manage them later")
        print("> maybe we should separate context management..")

    def addContext(self):
        ok=False
        dialog=QtGui.QInputDialog.getText(self,"New Context","Please enter new context name",QtGui.QLineEdit.Normal,"",ok)
        if dialog[0] and dialog[1]:
            self.db.addContext(str(dialog[0]))
            self.loadContexts()
        
    def removeContext(self):
        if self.currentContext==1:
            QtGui.QMessageBox.critical(self,"Error","Removal of first context is not possible atm. TBD later")
            #TODO: some settings table with saved last opened context
        else:
            if self.questionPopup("Remove context", "Do you really want to remove active context?"):
                self.db.deleteContext(self.currentContext)
                self.currentContext=1 #TODO: change it to first available
                self.loadTasksList()
                self.loadContexts()


# CONTEXT MANAGEMENT:

    def loadContexts(self):
        self.contexts={}
        self.ui.menuContext.clear()
        
        for i in self.db.getContexts():
            item=QtGui.QAction(self.ui.menuContext)
            item.setText(i[1])
            item.setCheckable(True)
            item.triggered.connect(lambda context=item: self.switchContext(context))
            item.setData(i[0])
            self.contexts[i[1]]=i[0]
            #item.triggered.connect(self.switchContext)
            self.ui.menuContext.addAction(item)
        self.ui.menuContext.addSeparator()
        newContext = QtGui.QAction(self.ui.menuContext)
        newContext.setText("Create new context")
        newContext.triggered.connect(self.addContext)
        self.ui.menuContext.addAction(newContext)
        removeContext = QtGui.QAction(self.ui.menuContext)
        removeContext.setText("Remove current context")
        removeContext.triggered.connect(self.removeContext)
        self.ui.menuContext.addAction(removeContext)
        self.ui.menuContext.children()[self.currentContext].setChecked(True)
        
    def switchContext(self,item):
        if item.isChecked():
            for i in self.ui.menuContext.children():
                if i!=item and i!=self.ui.menuContext.children()[0]:
                    i.setChecked(False)
            self.currentContext=self.contexts[str(item.text())]
            self.loadTasksList()
        else:
            item.setChecked(True)
            

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = Workload(app)

    res = app.exec_()
    sys.exit()
