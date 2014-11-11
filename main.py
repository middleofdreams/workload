# -*- coding: utf-8 -*-
from PySide import QtGui,QtCore
from ui.main_ui import Ui_MainWindow
from db import DB
from task import Task
from tray import Trayicon
from settingsWindow import SettingsWindow
from settings import Settings
from contexts import loadContexts,selectCurrentContext
from archive import ArchiveWindow
class Workload(QtGui.QMainWindow):

    def __init__(self,app):
        '''main window init'''
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setStyleSheet('ui/style.qss')
        windowBG="(219,237,255,200)"
        windowFrame="(85, 170, 255,150)"
        selectedMenuItemBG="(85, 170, 220,80)"
        alternateListItem="(170,213,255,250)"
        WindowStyle="QMainWindow{border:2px solid rgba"+windowFrame+";  border-radius: 2px;background-color:rgba"+windowBG+";}"
        StatusbarStyle="QStatusBar{background-color:transparent;border-top: 0px transparent; border-radius:2px;\
        border-bottom: 3px solid rgba(85, 170, 255,150);border-left: 2px solid rgba(85, 170, 255,150);border-right: 2px solid rgba(85, 170, 255,150)}"
        MenubarStyle="QMenuBar{padding:2px 2px;background-color:rgba"+windowBG+";border-top: 3px solid rgba(85, 170, 255,150);\
        border-left:2px solid rgba(85, 170, 255,150);border-right: 2px solid rgba(85, 170, 255,150);border-radius: 2px}\
        QMenuBar::item{padding: 2px 2px;background-color:transparent;color:rgb(55, 55, 55);border-radius:3px}"
        MenuStyle="QMenu{background-color:rgba"+windowBG+";color:black;border:1px solid rgba"+windowFrame+";\
        border-left:3px solid rgba(85, 170, 255,80);border-radius:3px} \
        QMenu::item{padding: 2px 20px;background-color:rgba"+windowBG+";color:rgb(55, 55, 55)}\
        QMenu::item::selected{background-color:rgba"+selectedMenuItemBG+";color:rgb(55, 55, 55);border:1px solid rgba(85, 170, 255,150);\
        border-radius:3px}QMenu::separator{background-color:rgba"+windowFrame+";border 1px solid:rgb(55,55,55);height:2px;margin-left:5px;margin-right:5px;}"
        TaskList="QTreeWidget{background-color:rgba"+windowBG+";alternate-background-color:rgba"+alternateListItem+"}"
        self.setStyleSheet(WindowStyle)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.taskList.setStyleSheet(TaskList)
        self.ui.menubar.setStyleSheet(MenubarStyle)
        self.ui.menuFile.setStyleSheet(MenuStyle)
        self.ui.menuTask.setStyleSheet(MenuStyle)
        self.ui.menuContext.setStyleSheet(MenuStyle)
        self.ui.statusbar.setStyleSheet(StatusbarStyle)
        
        #GUI setting
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint
                            | QtCore.Qt.WindowStaysOnTopHint)
        
        desktop = QtGui.QApplication.desktop()
        if desktop.height() > 800:
            self.move(10, (desktop.height() / 2) - (self.height()))
        else:
            self.move(15, 150)
        self.resizeColumns()
        
        
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
        self.ui.actionSettings.triggered.connect(lambda s=self:SettingsWindow(s))
        self.ui.actionExport_tasklist.triggered.connect(self.exportTaskList)
        self.ui.taskInput.dropEvent = self.dropTask
# SET VARIABLES AND CONNECT TO DB:

        self.taskOpened = False
        self.app = app
        self.db = DB(self)
        self.settings=Settings(self)
        loadContexts(self)
        self.currentContext = self.settings.getInitContext()
        selectCurrentContext(self)
        self.loadTasksList(init=True)  
        self.tray=Trayicon(self)
        
        self.show()

        self.adjustHeight(downSize=True, init=False)
        self.ui.statusbar.showMessage("Hello! Ready to work ;-)",3600)
    
    def dropTask(self,e):
        Task.dropTask(self, e)
    
    def resizeEvent(self,e):
        self.resizeColumns()
        
    def resizeColumns(self):
        self.ui.taskList.setColumnWidth(0, 20)
        self.ui.taskList.setColumnWidth(2, 10)
        self.ui.taskList.setColumnWidth(1, self.width()-45)
        
    def setMarker(self):
        print("set icon in column 2 when task is notification time")
           
# TASKS RELATED ACTIONS
    def addTask(self,e):
        print(e)
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
        if len(t)>20:
            taskname=t[:20]+"..."
            taskDescription=t
        else:
            taskname=t
            taskDescription=""
        if self.checkIfExist(taskname) is not True:  
            taskid = self.db.addTask(taskname,priority, taskDescription, duedate, self.currentContext)
            self.createTaskItem(taskname, taskid, priority)
            self.adjustHeight()
            self.ui.statusbar.showMessage("New task created.",3300)
        else:
            self.ui.taskInput.setText(taskname)
            self.taskAlreadyExistMsg(self)
            
    def createTaskItem(self, t, taskid=None, priority=0):
        item = QtGui.QTreeWidgetItem([str(priority), t])
        item.setData(0, 32, taskid)
        item.setSizeHint(0, QtCore.QSize(0, 22))
        self.ui.taskList.addTopLevelItem(item)
        self.setPriorityColor(item, priority)
        self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)
        
        
    def checkIfExist(self,t):
        if len(self.ui.taskList.findItems(t,QtCore.Qt.MatchFlags(QtCore.Qt.MatchExactly),1))>0:
            return True
            
            
    def taskAlreadyExistMsg(self,parent):
        text="Task with same name already exist, choose another"
        msg = QtGui.QMessageBox.information(parent, "Task name already exist", text, buttons=QtGui.QMessageBox.Ok )

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
            self.ui.statusbar.showMessage("Task removed.",3300)


    def setTaskPriority(self,priority):
        selectedItems = self.ui.taskList.selectedItems()
        for item in selectedItems:
            self.db.setTaskPriority(item.data(0, 32),priority)
            self.setPriorityColor(item, priority)
            item.setText(0,str(priority))
            self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)
            self.ui.statusbar.showMessage("Priority updated.",3300)

    def setPriorityColor(self,item,priority):
        icon=QtGui.QIcon(':priority/status/'+str(priority)+'.png')
        item.setIcon(0,icon)
        item.setTextAlignment(0,QtCore.Qt.AlignCenter)

    def openTask(self):
        if not self.taskOpened:
            item = self.getSelectedItem()
            if item:
                Task(self,item.data(0, 32))
            

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
        if e.buttons() & QtCore.Qt.LeftButton:
            try:
                self.posx
                self.posy
            except:
                self.posx=e.x()
                self.posy=e.y()
            y=e.globalY()-self.posy
            x=e.globalX()-self.posx
            self.move(x,y)
            #e.accept()


    def mouseReleaseEvent(self, e):
        try:
            del(self.posx)
            del(self.posy)
        except:
            pass
        
    def adjustHeight(self,downSize=False,init=False):
        tasks=self.db.getTasks(self.currentContext)
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
            
    def exportTaskList(self):
        fname=QtGui.QFileDialog.getSaveFileName()#"Select file to save task list")
        if fname:
            includeArchive=self.questionPopup("Exporting tasks", "Do you want to include completed tasks?")
            tasks=self.db.exportTasks(self.currentContext, includeArchive)
            from lib import importexport
            importexport.export(tasks, fname[0],self.settings.getDateFormat())
            
    def about(self):
        f=open("about.html")
        text=f.read()
        f.close()
        about = QtGui.QMessageBox.information(self, "About", text, buttons=QtGui.QMessageBox.Ok )

    def exit(self):
        if self.questionPopup("Exit", "Are you sure?"):
            self.settings.setCurrentContextAsLast()
            self.app.exit()

    def createTask(self):
        Task(self,taskid=0)

    def completeTasks(self):
        tasks=self.ui.taskList.selectedItems()
        for i in tasks:
            self.db.completeTask(i.data(0,32))
            index = self.ui.taskList.indexOfTopLevelItem(i)
            self.ui.taskList.takeTopLevelItem(index)
            self.ui.statusbar.showMessage("Task completed.",3300)

    def showHistory(self):
        ArchiveWindow(self)
                


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = Workload(app)

    res = app.exec_()
    sys.exit()
