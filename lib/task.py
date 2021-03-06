# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
from ui.task_ui import Ui_Dialog
import datetime,unicodedata
from lib.helpers import timestamp,QtDateFormat
from lib.style import changeStyle

class Task(QtGui.QDialog):
    def __init__(self,parent,taskid,taskname=None,description=None):
        '''main window init'''
        parent.taskOpened=True
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint
                            | QtCore.Qt.WindowStaysOnTopHint)
        self.parent=parent
        self.settings=self.parent.settings
        self.taskid=taskid
        #self.moveIt=False
        statusbar=QtGui.QStatusBar(self)
        self.ui.verticalLayout.addWidget(statusbar)
        
        fontlist=self.settings["chosenFonts"].split("|")
        for i in fontlist:
            if i in fontlist:
                self.ui.fontComboBox.addItem(i,None)
        
        windowOpacity=int(self.settings["taskWindowOpacity"])/100
        self.setWindowOpacity(float(windowOpacity))
        self.setProperty("dialog","taskEditor")
        editorButtons=[self.ui.editorBGcolor,self.ui.editorTextColor,self.ui.editorResetColor]
        for i in editorButtons:
            i.setProperty("button","taskEditor")
        self.ui.editorBold.setProperty("button", "taskEditorBold")
        self.ui.editorItalic.setProperty("button", "taskEditorItalic")
        self.ui.editorUnderline.setProperty("button", "taskEditorUnderline")
        self.ui.label_4.setProperty("label","bold")
        self.ui.label_6.setProperty("label","bold")
        self.ui.label_3.setProperty("label","bold")
        changeStyle(self)
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
        self.ui.taskName.focusInEvent=self.taskNameFocus
        self.ui.taskDescription.event=self.eventFilter
        self.task=self.parent.db.getTaskDetails(taskid)
        if self.taskid:
            self.ui.label_6.hide()  #Hide closed date label
            self.ui.dueDate.setDisplayFormat(QtDateFormat(self.settings["dateFormat"]))
            self.setWindowTitle(self.task["name"])
            self.ui.taskName.setText(self.task["name"])
            self.ui.priority.setValue(int(self.task["priority"]))
            self.setPriorityText(int(self.task["priority"]))
            desc=self.task["taskdescription"]
            self.ui.taskDescription.append(desc)
            createdTimestamp=int(self.task["created"].split(".")[0])
            createdDate=datetime.datetime.fromtimestamp(createdTimestamp)
            createdDate=createdDate.strftime(self.settings["dateFormat"])
            self.ui.createDate.setText(createdDate)
            
            if self.task["closedat"] is not None:
                self.ui.label_6.show()
                closeTimestamp=int(self.task["closedat"].split(".")[0])
                closeDate=datetime.datetime.fromtimestamp(closeTimestamp)
                closeDate=closeDate.strftime(self.settings["dateFormat"])
                self.ui.closeDate.setText(closeDate)
                self.ui.buttonBox.buttons()[0].setDisabled(True)
            
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
            
            self.setWindowTitle(self.tr("Create New Task"))
            if description is not None:
                self.ui.taskDescription.append(description)
            if taskname is not None:
                self.ui.taskName.setText(taskname)
                self.ui.taskName.setFocus()
                self.ui.taskName.deselect()
                self.ui.taskName.end(True)
            else:
                if self.parent.ui.taskInput.text()=="":
                    self.ui.taskName.setText(self.tr("Enter task name here"))
                else:
                    self.ui.taskName.setText(self.parent.ui.taskInput.text())
                    self.parent.ui.taskInput.clear()
            self.setPriorityText(0)
            date=datetime.datetime.now()
            delta=datetime.timedelta(hours=24)
            date=date+delta
            self.ui.dueDate.setDateTime(QtCore.QDateTime(date.year,date.month,date.day,date.hour,date.minute,0,0))
        self.move(self.parent.pos())
        self.exec_()
        parent.taskOpened=False
    
    def taskNameFocus(self,e):
        pass
    
    def eventFilter(self,e):
        if e.type()==QtCore.QEvent.KeyPress:
            #print(e.key())
            if e.key()==QtCore.Qt.Key_Tab:
                self.insertTabs()
                return True
            if e.key()==QtCore.Qt.Key_Backtab:
                self.removeTabs()
                return True
            elif e.key()==82:
                if (QtCore.Qt.ControlModifier & e.modifiers()):
                    self.resetColors()
                    return True
            elif e.key()==66:
                if (QtCore.Qt.ControlModifier & e.modifiers()):
                    self.setFontBold()
                    return True
            elif e.key()==85:
                if (QtCore.Qt.ControlModifier & e.modifiers()):
                    self.setFontUnderline()
                    return True
            elif e.key()==73:
                if (QtCore.Qt.ControlModifier & e.modifiers()):
                    self.setFontItalic()
                    return True
            elif e.key()==83:
                if (QtCore.Qt.ControlModifier & e.modifiers()):
                    self.saveTaskDetails()
                    return True
        return QtGui.QTextBrowser.event(self.ui.taskDescription,e)
       
    def insertTabs(self):
        cursor=self.ui.taskDescription.textCursor()
        if cursor.hasSelection():
            s1=cursor.selectionStart()
            s2=cursor.selectionEnd()
            cursor.setPosition(s1)
            cursor.movePosition(QtGui.QTextCursor.StartOfLine,QtGui.QTextCursor.MoveAnchor,s1)
            cursor.setPosition(s2,QtGui.QTextCursor.KeepAnchor)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine,QtGui.QTextCursor.KeepAnchor,s2)
            self.ui.taskDescription.setTextCursor(cursor)
            s2=cursor.selectionEnd()
        selectedText=cursor.selectedText()
        data=""
        if selectedText!="":
            for i in selectedText.splitlines():
                if i!="":
                    i="\t"+i+"\n"
                data+=i
            cursor.insertText(data.rstrip("\n"))
            s2=cursor.position()
            cursor.setPosition(s1)
            cursor.movePosition(QtGui.QTextCursor.StartOfLine,QtGui.QTextCursor.MoveAnchor,s1)
            cursor.setPosition(s2,QtGui.QTextCursor.KeepAnchor)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine,QtGui.QTextCursor.KeepAnchor,s2)
            self.ui.taskDescription.setTextCursor(cursor)
        else:
            cursor.insertText("\t")
        
    def removeTabs(self):
        cursor=self.ui.taskDescription.textCursor()
        if cursor.hasSelection():
            s1=cursor.selectionStart()
            s2=cursor.selectionEnd()
            cursor.setPosition(s1)
            cursor.movePosition(QtGui.QTextCursor.StartOfLine,QtGui.QTextCursor.MoveAnchor,s1)
            cursor.setPosition(s2,QtGui.QTextCursor.KeepAnchor)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine,QtGui.QTextCursor.KeepAnchor,s2)
            self.ui.taskDescription.setTextCursor(cursor)
            newtext=""
            selectedText=cursor.selectedText()
            if selectedText!="":
                for i in selectedText.splitlines():
                    if i!="":
                        i=bytes(i,"utf-8")
                        if i[:1]==b"\t" or i[:1]==b" ":
                            i=i[1:]                 
                        i=i.decode("utf-8")+"\n"
                    newtext+=i
            cursor.insertText(newtext.rstrip("\n"))
            s2=cursor.position()
            cursor.setPosition(s1)
            cursor.setPosition(s2,QtGui.QTextCursor.KeepAnchor)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine,QtGui.QTextCursor.KeepAnchor,s2)
            self.ui.taskDescription.setTextCursor(cursor)
        else:
            s1=cursor.position()
            cursor.setPosition(s1)
            cursor.movePosition(QtGui.QTextCursor.StartOfLine,QtGui.QTextCursor.MoveAnchor,s1)
            cursor.movePosition(QtGui.QTextCursor.EndOfLine,QtGui.QTextCursor.KeepAnchor,s1)
            self.ui.taskDescription.setTextCursor(cursor)
    
    def resizeEvent(self,e):
        path=QtGui.QPainterPath()
        rect=self.size()
        path.addRoundedRect(-1,-1,rect.width()+1,rect.height()+1,10,10)
        region=QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)
        e.accept()
                
    def setPriorityText(self,priority):
        priorities=[self.tr("Not set!"),self.tr("Now"),self.tr("Next"),self.tr("Later"),self.tr("Someday"),self.tr("Awaiting")]
        self.ui.priorityText.setText(priorities[priority])
        
    def setDueOn(self,e):
        if e==2:
            self.ui.dueDate.setEnabled(True)
        else:
            self.ui.dueDate.setDisabled(True)
        
    def setStylesForButtons(self,setButton,color):
        styleSheet="QPushButton[Button=color] {margin-left:1px; border: 1px solid rgba(0, 0, 0,190);  border-radius: 2px;border-style: outset; background-color:rgba"+str(color)+"}"
        setButton.setProperty('Button','color')
        setButton.setStyleSheet(styleSheet)
        
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
    
    def saveTaskDetails(self):
        taskid=self.taskid
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
            self.parent.ui.statusbar.showMessage(self.tr("Task updated"),3300)
        else:
            self.taskAlreadyExistMsg=self.parent.taskAlreadyExistMsg
            self.taskAlreadyExistMsg(self)
        
    def updateItem(self,taskname,priority):
        selectedItems = self.parent.ui.taskList.selectedItems()
        for item in selectedItems:
            self.parent.setPriorityColor(item, priority)
            item.setText(0,str(priority))
            item.setText(2,str(taskname))
            self.parent.ui.taskList.sortItems(0,QtCore.Qt.AscendingOrder)
    
    def openHyperlink(self,e):
        QtGui.QDesktopServices.openUrl(e)
        
    def accept(self):
        taskid=self.taskid
        if taskid!=0:    
            #save task details
            self.saveTaskDetails()
            self.close()
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
                self.parent.ui.statusbar.showMessage(self.tr("New task created."),3300)
            else:
                self.parent.taskAlreadyExistMsg(parent=self)
        self.parent.timer.getNearEndTasks(force=True)

    def dropTask(self,e):
            fulldata=e.mimeData().text()    
            self.ui.statusbar.showMessage(self.tr("New task created."),3300)
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
        cursor=self.ui.taskDescription.textCursor()
        if cursor.hasSelection():
            bgColor=QtGui.QColor(255,255,255)
            textColor=QtGui.QColor(0,0,0)
            self.ui.taskDescription.setTextColor(textColor)
            self.ui.taskDescription.setTextBackgroundColor(bgColor)
            
