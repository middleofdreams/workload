# -*- coding: utf-8 -*-
from PySide import QtGui,QtCore
from ui.main_ui import Ui_MainWindow
from lib.db import DB
from lib.task import Task
from lib.tray import Trayicon
from lib.settings import Settings
from lib.contexts import loadContexts,selectCurrentContext
from lib.archive import ArchiveWindow
from lib.timer import TaskReminder
import datetime
from lib.helpers import timestamp
from lib.shortcuts import ShortcutsHandler
from lib.GuiManager import guiSettings,connectSignals, finalizeInit
from lib.style import changeStyle

class Workload(QtGui.QMainWindow):

    def __init__(self,app,onlyDBAccess=False):
        '''main window init'''
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = DB(self)
        self.settings=Settings(self)
        self.onlyDBAccess=onlyDBAccess
        if onlyDBAccess:
            return 
        #GUI setting
        guiSettings(self)
        connectSignals(self)
        changeStyle(self)
        
        self.taskOpened = False
        self.app = app
        loadContexts(self)
        self.currentContext = self.settings.getInitContext()
        selectCurrentContext(self)
        self.loadTasksList(init=True)  
        self.tray=Trayicon(self)
        self.timer=TaskReminder(self)
        self.shortcuts=ShortcutsHandler(self,self.settings['keyMainWindowToggle'])
        finalizeInit(self)
        self.translate()
        self.adjustHeight(init=True)


    def resizeEvent(self,e):
       
        path=QtGui.QPainterPath()
        rect=e.size()
        path.addRoundedRect(-1,-1,rect.width()+1,rect.height()+1,7,7)
        region=QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
        


    def taskListFocusIn(self,e):
        if e.reason()==QtCore.Qt.FocusReason.TabFocusReason:
            try:
                item=self.ui.taskList.itemAt(0)
                self.ui.taskList.setCurrentItem(self.ui.taskList.itemAt(0))
            except:
                pass
    def toggle(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            
    def dropTask(self,e):
        Task.dropTask(self, e)
        
    def resizeColumns(self):
        self.ui.taskList.setColumnWidth(0, 20)
        self.ui.taskList.setColumnWidth(1, 20)
        self.ui.taskList.hideColumn(0)

        
    def setMarker(self,tasks):
        icon=QtGui.QIcon(':res/status/clock.png')
        items=self.ui.taskList.findItems("",QtCore.Qt.MatchContains|QtCore.Qt.MatchRecursive)
        for i in items:
            removeicon=QtGui.QIcon()
            i.setIcon(2,removeicon)
        for i in tasks:
            for j in items:
                if j.data(0,32)==i:
                    j.setIcon(2,icon)
    
                    
    def drawRow(self,painter,myopt,index):
        myopt.decorationPosition=QtGui.QStyleOptionViewItem.Right
        myopt.decorationAlignment=QtCore.Qt.AlignCenter
        QtGui.QTreeWidget.drawRow(self.ui.taskList,painter,myopt,index)
        
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
#TODO: create new function to handle input (regexp etc)
        if len(t)>50:
            taskname=t[:50]
            taskDescription=t
        else:
            taskname=t
            taskDescription=""
        if self.checkIfExist(taskname) is not True:
            duedate=self.defaultDueDate()  
            taskid = self.db.addTask(taskname,priority, taskDescription, duedate, self.currentContext)
            self.createTaskItem(taskname, taskid, priority)
            self.adjustHeight()
            self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","New task created."),3300)
        else:
            self.ui.taskInput.setText(taskname)
            self.taskAlreadyExistMsg()
            
    def defaultDueDate(self):
        if self.settings["defaultDueDateOn"]:
            dueValue=int(self.settings["defaultDueDateValue"])
            if self.settings["defaultDueDateUnit"]=="0":
                td=datetime.timedelta(hours=dueValue)
            else:
                td=datetime.timedelta(days=dueValue)
            return timestamp(datetime.datetime.now()+td)
        else:
            return None
            
    def createTaskItem(self, t, taskid=None, priority=0):
        item = QtGui.QTreeWidgetItem([str(priority),"", t])
        item.setData(0, 32, taskid)
        item.setSizeHint(1, QtCore.QSize(0, 22))
        self.ui.taskList.addTopLevelItem(item)
        self.setPriorityColor(item, priority)
        self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)
        
    def checkIfExist(self,t):
        if len(self.ui.taskList.findItems(t,QtCore.Qt.MatchFlags(QtCore.Qt.MatchExactly),2))>0:
            return True
            
            
    def taskAlreadyExistMsg(self,parent=None):
        text=QtGui.QApplication.translate("ui","Task with same name already exist, choose another")
        windowtitle=QtGui.QApplication.translate("ui","Task name already exists")
        msgWindow=QtGui.QMessageBox()
        if parent is not None: self=parent
        msgWindow.information(self, windowtitle, text, buttons=QtGui.QMessageBox.Ok )
    
    def loadTasksList(self, archived=False,init=False):
        self.ui.taskList.clear()
        for i in self.db.getTasks(self.currentContext):
            self.createTaskItem(i[1], i[0],i[2])

    def deleteSelectedTasks(self, force=False):
        selectedItems = self.ui.taskList.selectedItems()
        if len(selectedItems)>0:
            tasks = []
            for item in selectedItems:
                tasks.append(item)
            windowtitle=QtGui.QApplication.translate("ui","Delete task")
            text=QtGui.QApplication.translate("ui","Do you really want to delete selected  task(s) ?")
            if force:
                self.deleteTasks(tasks)
                windowtitle=QtGui.QApplication.translate("ui","Delete task")
                text=QtGui.QApplication.translate("ui","Do you really want to delete selected  task(s) ?")
            elif self.questionPopup(windowtitle,text):
                self.deleteTasks(tasks)
            self.adjustHeight(downSize=True)

    def deleteTasks(self, tasks):
        for item in tasks:
            self.db.deleteTask(item.data(0, 32))
            index = self.ui.taskList.indexOfTopLevelItem(item)
            self.ui.taskList.takeTopLevelItem(index)
            self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","Task removed."),3300)


    def setTaskPriority(self,priority):
        selectedItems = self.ui.taskList.selectedItems()
        for item in selectedItems:
            self.db.setTaskPriority(item.data(0, 32),priority)
            self.setPriorityColor(item, priority)
            item.setText(0,str(priority))
            self.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)
            self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","Priority updated."),3300)
            
    def setPriorityColor(self,item,priority):
        icon=QtGui.QIcon(':res/status/'+str(priority)+'.png')
        item.setIcon(1,icon)

    def openTask(self,taskname=None):
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
            if (QtCore.Qt.ShiftModifier & e.modifiers()):
                self.deleteSelectedTasks(True)
        elif e.key()>48 and e.key()<54:
            self.setTaskPriority(e.key()-48)
        elif e.key()==78:
            self.ui.taskInput.setFocus()
        else:
            QtGui.QTreeWidget.keyPressEvent(self.ui.taskList,e)


    def getKeysOnInput(self, e):
        if e.key()==16777221 or e.key()==16777220:  # enter/return
            if (QtCore.Qt.AltModifier & e.modifiers()):
                self.createTask()
            else:
                self.addTask()
        else:
            QtGui.QLineEdit.keyPressEvent(self.ui.taskInput,e)
            input=self.ui.taskInput.text()
            if len(input)>50:
                taskname=input[:50].strip()
                taskname=taskname.replace("\r\n","\n")
                taskname=taskname.replace("\n"," ")
                taskname=taskname.replace("\t"," ")
                taskname=taskname.replace("  ","")
                description=input
                Task(self,taskid=0,taskname=taskname,description=description)
                self.ui.taskInput.clear()

    #ADDITIONAL FUNTIONS
    def questionPopup(self, title, msg):
        window=QtGui.QMessageBox()
        window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        resp = window.question(self, title, msg,
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
        if len(tasks)>0:
            item=self.ui.taskList.topLevelItem(0)
            qmodel=self.ui.taskList.indexFromItem(item)
            
            taskheight=self.ui.taskList.rowHeight(qmodel)
        else:
            taskheight=22
        if init:
            winheight=320
            listheight=252
        else:
            winheight=self.height()
            listheight=self.ui.taskList.height()
        desiredHeight=taskheight*len(tasks)+winheight-listheight+6
        if ( desiredHeight>self.height() or downSize ) and desiredHeight<QtGui.QApplication.desktop().height():
            self.resize(self.width(),desiredHeight)

    def closeEvent(self, e=None):
        self.hide()
        if e:
            e.ignore()

###### MENU FUNCTIONS

    def importTasklist(self):
        fname=QtGui.QFileDialog.getOpenFileName(self, QtGui.QApplication.translate("ui","Open"), "", QtGui.QApplication.translate("ui","Workload Import File (*.w)"))
        if dialog[0]:
            filename=fname[0]
            from lib import importexport
            importexport.importTasks(self,filename,self.settings["dateFormat"])
            
    def exportTaskList(self):
        fname=QtGui.QFileDialog.getSaveFileName(self,QtGui.QApplication.translate("ui","Save"), "", QtGui.QApplication.translate("ui","Workload Export File (*.w)"))
        if fname[0]:
            includeArchive=self.questionPopup(QtGui.QApplication.translate("ui","Exporting tasks"), QtGui.QApplication.translate("ui","Do you want to include completed tasks?"))
            tasks=self.db.exportTasks(self.currentContext, includeArchive)
            from lib import importexport
            filename=fname[0]
            importexport.export(tasks, filename,self.settings["dateFormat"])
            
    def about(self):
        f=open("about.html")
        text=f.read()
        f.close()
        QtGui.QMessageBox.information(self, QtGui.QApplication.translate("ui","About"), text, buttons=QtGui.QMessageBox.Ok )

    def exit(self,exitcode=0):
        exit_=False
        if self.settings["askOnExit"]:
            if self.questionPopup(QtGui.QApplication.translate("ui","Exit"), QtGui.QApplication.translate("ui","Are you sure?")):
                exit_=True
        else: exit_=True
        if exit_==True:
            self.settings.setCurrentContextAsLast()
            self.shortcuts.terminate()
            self.app.exit(exitcode)

    def createTask(self):
        Task(self,taskid=0)

    def completeTasks(self):
        if self.ui.taskList.hasFocus():
            tasks=self.ui.taskList.selectedItems()
            for i in tasks:
                self.db.completeTask(i.data(0,32))
                index = self.ui.taskList.indexOfTopLevelItem(i)
                self.ui.taskList.takeTopLevelItem(index)
                self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","Task completed."),3300)

    def showHistory(self):
        ArchiveWindow(self)
                
    def hoyKeyError(self):
        QtGui.QMessageBox.critical(self,QtGui.QApplication.translate("ui","Error"),QtGui.QApplication.translate("ui","Unable to register global shortcut"))

    def changeEvent(self, e):
        if e.type()==QtCore.QEvent.LanguageChange:
            self.ui.retranslateUi(self)
            self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","Hello! Ready to work ;-)"),3600)
            loadContexts(self)
            selectCurrentContext(self)
            
        QtGui.QMainWindow.changeEvent(self,e)
        
    def translate(self,lang=None):
        if lang is None:
            lang= self.settings["lang"]
        translate=True
        if lang=="auto":
            locale = QtCore.QLocale.system().name()
        
        elif lang=="en":
            translate=False
            try:
                self.app.removeTranslator(self.qtTranslator)
            except:
                pass
        else:
            locale=lang
    
        if translate:
            self.qtTranslator = QtCore.QTranslator()
            self.qtTranslator.load("i18n"+os.sep+"workload_"+locale+".qm")
            self.app.installTranslator(self.qtTranslator)
    def showMsg(self,msg):
        msgWindow=QtGui.QMessageBox()
        msgWindow.information(self, "Workload - Information", msg, buttons=QtGui.QMessageBox.Ok )
      
  
if __name__ == "__main__":
    import sys,os

    exitcode=1
    app = QtGui.QApplication(sys.argv)
    myapp = Workload(app)



        #app.languageChange()

    sys.exit(app.exec_())
