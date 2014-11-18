# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from ui.task_ui import Ui_Dialog
import datetime,unicodedata
from lib.helpers import timestamp,QtDateFormat
class Task(QtGui.QDialog):

    def __init__(self,parent,taskid):
        '''main window init'''
        parent.taskOpened=True
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint
                            | QtCore.Qt.WindowStaysOnTopHint)
        self.parent=parent
        self.taskid=taskid
        self.moveIt=False        
        
        
#Text Editor
        fontlist=self.parent.settings["chosenFonts"].split("|")  #TODO: read font settings from database
        for i in fontlist:
            if i in fontlist:
                self.ui.fontComboBox.addItem(i,None)
        
        WindowStyle="QDialog{border: 2px solid rgba(55, 55, 55,222);  border-radius: 6px; background-color:rgba(255,255,230,250)}"
        self.setStyleSheet(WindowStyle)
        windowOpacity=int(self.parent.settings["taskWindowOpacity"])/100
        self.setWindowOpacity(float(windowOpacity))
        self.ui.dueOn.stateChanged.connect(self.setDueOn)
        self.ui.priority.valueChanged.connect(self.setPriorityText)
        self.ui.taskDescription.cursorPositionChanged.connect(self.toggleFont)
        self.ui.fontComboBox.activated.connect(self.setEditorFont)
        self.ui.fontSize.valueChanged.connect(self.setEditorFont)
        self.ui.editorBold.clicked.connect(self.setFontBold)
        self.ui.editorItalic.clicked.connect(self.setFontItalic)
        self.ui.editorUnderline.clicked.connect(self.setFontUnderline)
        self.ui.editorBGcolor.clicked.connect(self.setBGcolor)
        self.ui.editorTextColor.clicked.connect(self.setTextColor)
        self.ui.currentBGcolor.clicked.connect(self.setCurrentBGcolor)
        self.ui.currentTextColor.clicked.connect(self.setCurrentTextColor)
        self.setStylesForButtons(self.ui.currentBGcolor, "(255,255,255,255)")
        self.setStylesForButtons(self.ui.currentTextColor, "(0,0,0,255)")
        self.ui.editorResetColor.clicked.connect(self.resetColors)
        self.ui.taskDescription.anchorClicked.connect(self.openHyperlink)
        
        self.task=self.parent.db.getTaskDetails(taskid)
        if self.taskid:
            self.ui.label_6.hide()  #Hide closed date label
            self.ui.dueDate.setDisplayFormat(QtDateFormat(self.parent.settings["dateFormat"]))
            self.setWindowTitle(self.task["name"])
            self.ui.taskName.setText(self.task["name"])
            self.ui.priority.setValue(self.task["priority"])
            self.setPriorityText(self.task["priority"])
            self.ui.taskDescription.append(self.task["taskdescription"])
            createdTimestamp=int(self.task["created"].split(".")[0])
            createdDate=datetime.datetime.fromtimestamp(createdTimestamp)
            createdDate=createdDate.strftime(self.parent.settings["dateFormat"])
            self.ui.createDate.setText(createdDate)
            
            if self.task["closedat"] is not None:
                self.ui.label_6.show()
                closeTimestamp=int(self.task["closedat"].split(".")[0])
                closeDate=datetime.datetime.fromtimestamp(closeTimestamp)
                closeDate=closeDate.strftime(self.parent.settings.getDateFormat())
                self.ui.closeDate.setText(closeDate)
            
            if self.task["due"] is not None:
                self.ui.dueOn.setChecked(True)
                timestamp=int(self.task["due"].split(".")[0])
                date=datetime.datetime.fromtimestamp(timestamp)
                self.ui.dueDate.setDateTime(QtCore.QDateTime(date.year,date.month,date.day,date.hour,date.minute,0,0))
            else:
                date=datetime.datetime.now()
                self.ui.dueDate.setDateTime(QtCore.QDateTime(date.year,date.month,date.day,date.hour,date.minute,0,0))
        else:
            self.ui.label_4.hide()  #Hide created date label
            self.ui.label_6.hide()  #Hide closed date label
            
            self.setWindowTitle("Create New Task")
            self.ui.taskName.setText("Enter task name here")
            self.setPriorityText(0)
            date=datetime.datetime.now()
            delta=datetime.timedelta(hours=24)
            date=date+delta
            self.ui.dueDate.setDateTime(QtCore.QDateTime(date.year,date.month,date.day,date.hour,date.minute,0,0))
        self.move(self.parent.pos())

        r=self.exec_()
        parent.taskOpened=False

        
    def setPriorityText(self,priority):
        priorities=["Not set!","Now","Next","Later","Someday","Awaiting"]
        self.ui.priorityText.setText(priorities[priority])
        
    def setDueOn(self,e):
        if e==2:
            self.ui.dueDate.setEnabled(True)
        else:
            self.ui.dueDate.setDisabled(True)
        
    def setStylesForButtons(self,setButton,color):
        styleSheet="QPushButton[Button=color] {height: 15px; border: 1px solid rgba(0, 0, 0,190);  border-radius: 2px;border-style: outset; background-color:rgba"+str(color)+"}"
        setButton.setStyleSheet(styleSheet)
        setButton.setProperty('Button','color')
        
    def closeEvent(self,e):
        #print(e)
        pass
        
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
        
    def updateItem(self,taskname,priority):
        selectedItems = self.parent.ui.taskList.selectedItems()
        for item in selectedItems:
            self.parent.setPriorityColor(item, priority)
            item.setText(0,str(priority))
            item.setText(1,str(taskname))
            self.parent.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)
    
    def openHyperlink(self,e):
        QtGui.QDesktopServices.openUrl(e)
        
    def accept(self):
        taskid=self.taskid
        if taskid!=0:    
            #save task details
            taskname=self.ui.taskName.text()
            if taskname==self.task["name"] or self.parent.checkIfExist(taskname) is not True:
                taskDescription=self.ui.taskDescription.toHtml()
                priority=int(self.ui.priority.text())
                if self.ui.dueOn.isChecked():
                    duedate=timestamp(self.ui.dueDate.dateTime().toPython())
                else:
                    duedate=None
                self.parent.db.setTaskDetails(taskid,taskDescription,priority,taskname,duedate)
                self.updateItem(taskname, priority)
                self.close()
                self.parent.ui.statusbar.showMessage("Task updated",3300)
            else:
                self.parent.taskAlreadyExistMsg(parent=self)
            
        else:
            #create new task
            taskname=self.ui.taskName.text()
            if self.parent.checkIfExist(taskname) is not True:
                priority=int(self.ui.priority.text())
                taskDescription=self.ui.taskDescription.toHtml()
                duedate=self.ui.dueDate.dateTime().toPython().timestamp()
                taskid = self.parent.db.addTask(taskname,priority,taskDescription, duedate, self.parent.currentContext)
                self.parent.createTaskItem(taskname, taskid, priority)
                self.parent.adjustHeight()
                self.close()
                self.parent.ui.statusbar.showMessage("New task created.",3300)
            else:
                self.parent.taskAlreadyExistMsg(parent=self)
        self.parent.timer.getNearEndTasks(force=True)

    def dropTask(self,e):
            fulldata=e.mimeData().text()    
            self.ui.statusbar.showMessage("New task created.",3300)
            date=datetime.datetime.now()
            delta=datetime.timedelta(hours=24)
            duedate=date+delta
            duedate=duedate.timestamp()
            priority=0   
            if len(fulldata) > 20:
                newdata=[]
                textFound=False
                for i in fulldata.splitlines():
                    if i.strip()!="" or textFound: 
                        newdata.append(i)
                        textFound=True
                newdata="\n".join(newdata)
                taskname=newdata[:50].strip()
                taskname=taskname.replace("\r\n","\n")
                taskname=taskname.replace("\n"," ")
                taskname=taskname.replace("\t"," ")
                taskname=taskname.replace("  ","")
                taskname=taskname[:50]+"..."
                taskDescription=newdata
                taskid = self.db.addTask(taskname,priority, taskDescription, duedate, self.currentContext)
                self.createTaskItem(taskname, taskid, priority=0)
                
            else:
                taskname=fulldata
                taskDescription=""
                taskid = self.db.addTask(taskname,priority, taskDescription, duedate, self.currentContext)
                self.createTaskItem(taskname, taskid, priority=0)
            
#Editor Functions 
    def toggleFont(self):
        currentFont=self.ui.taskDescription.currentFont().family()
        currentSize=self.ui.taskDescription.currentFont().pointSize()
        currentIndex=self.ui.fontComboBox.findText(currentFont)

        if not self.ui.taskDescription.textCursor().hasSelection():
            if currentIndex is not None:
                self.ui.fontComboBox.setCurrentIndex(currentIndex)
        self.ui.fontSize.setValue(currentSize)
           
            
    def setEditorFont(self):
        Editor=self.ui.taskDescription
        selection=Editor.textCursor()
        fontName=self.ui.fontComboBox.currentText()
        fontSize=int(self.ui.fontSize.text())
        f=Editor.currentFont()
        f.setFamily(fontName)
        f.setPointSize(fontSize)

        if selection.hasSelection():
            Editor.setCurrentFont(f)
            Editor.setFocus()
        else:
            Editor.setCurrentFont(f)
            Editor.setFocus()
      
    def setFontBold(self):
        f=self.ui.taskDescription.currentFont()
        if not self.ui.editorBold.isFlat():
            self.ui.editorBold.setFlat(True)
            f.setBold(True)
        else:
            self.ui.editorBold.setFlat(False)
            f.setBold(False)
        self.ui.taskDescription.setCurrentFont(f)
 
   
    def setFontItalic(self):
        f=self.ui.taskDescription.currentFont()
        if not self.ui.editorItalic.isFlat():
            self.ui.editorItalic.setFlat(True)
            f.setItalic(True)
        else:
            self.ui.editorItalic.setFlat(False)
            f.setItalic(False)
        self.ui.taskDescription.setCurrentFont(f)
            
    def setFontUnderline(self):
        f=self.ui.taskDescription.currentFont()
        if not self.ui.editorUnderline.isFlat():
            self.ui.editorUnderline.setFlat(True)
            f.setUnderline(True)
        else:
            self.ui.editorUnderline.setFlat(False)
            f.setUnderline(False)
        self.ui.taskDescription.setCurrentFont(f)
    
    def setBGcolor(self):
        currentColor=self.ui.currentBGcolor.palette().button().color()
        newColor=QtGui.QColorDialog.getColor(parent=self.parent)
        if newColor!=QtGui.QColor():
            self.ui.taskDescription.setTextBackgroundColor(newColor)
            self.setStylesForButtons(self.ui.currentBGcolor, newColor.getRgb())
        else:
            self.setStylesForButtons(self.ui.currentBGcolor, currentColor.getRgb())
        
    def setTextColor(self):
        currentColor=self.ui.currentTextColor.palette().button().color()
        newColor=QtGui.QColorDialog.getColor(parent=self.parent)
        if newColor!=QtGui.QColor():
            self.ui.taskDescription.setTextColor(newColor)
            self.setStylesForButtons(self.ui.currentTextColor, newColor.getRgb())
        else:
            self.setStylesForButtons(self.ui.currentTextColor, currentColor.getRgb())
            
    def setCurrentBGcolor(self):
        color=self.ui.currentBGcolor.palette().button().color()
        self.ui.taskDescription.setTextBackgroundColor(color)
    
    def setCurrentTextColor(self):
        color=self.ui.currentTextColor.palette().button().color()
        self.ui.taskDescription.setTextColor(color)
    
    def resetColors(self):
        self.setStylesForButtons(self.ui.currentBGcolor, color="(255,255,255,255)")
        self.setStylesForButtons(self.ui.currentTextColor, color="(0,0,0,255)")
