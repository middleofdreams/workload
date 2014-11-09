from PySide import QtGui, QtCore
from ui.task_ui import Ui_Dialog
import datetime

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
        self.ui.priority.valueChanged.connect(self.setPriorityText)
#Text Editor
        fontlist=["monofur","Times New Roman","Arial","DejaVu Serif"]  #TODO: read font settings from database
        fontlist.sort()
        for i in fontlist:
            self.ui.fontComboBox.addItem(i,None)
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
        self.task=self.parent.db.getTaskDetails(taskid)
        if self.taskid:
            self.ui.label_6.hide()  #Hide closed date label
            self.ui.dueDate.setDisplayFormat("dd-MM-yyyy HH:mm")
            self.setWindowTitle(self.task["name"])
            self.ui.taskName.setText(self.task["name"])
            self.ui.priority.setValue(self.task["priority"])
            self.setPriorityText(self.task["priority"])
            self.ui.taskDescription.setText(self.task["taskdescription"])
            
            createdTimestamp=int(self.task["created"].split(".")[0])
            createdDate=datetime.datetime.fromtimestamp(createdTimestamp)
            createdDate=createdDate.strftime("%d-%m-%Y %H:%M")
            self.ui.createDate.setText(createdDate)
            
            if self.task["closedat"] is not None:
                self.ui.label_6.show()
                closeTimestamp=int(self.task["closedat"].split(".")[0])
                closeDate=datetime.datetime.fromtimestamp(closeTimestamp)
                closeDate=closeDate.strftime("%d-%m-%Y %H:%M")
                self.ui.closeDate.setText(closeDate)
            
            if self.task["due"] is not None:
                timestamp=int(self.task["due"].split(".")[0])
                date=datetime.datetime.fromtimestamp(timestamp)
                self.ui.dueDate.setDateTime(QtCore.QDateTime(date.year,date.month,date.day,date.hour,date.minute,0,0))
            else:
                date=datetime.datetime.now()
                delta=datetime.timedelta(hours=24)
                date=date+delta
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
      
    def accept(self):
        taskid=self.taskid
        if taskid!=0:    
            #save task details
            taskDescription=self.ui.taskDescription.toHtml()
            priority=int(self.ui.priority.text())
            taskname=self.ui.taskName.text()
            duedate=self.ui.dueDate.dateTime().toPython().timestamp()
            self.parent.db.setTaskDetails(taskid,taskDescription,priority,taskname,duedate)
            self.updateItem(taskname, priority)
            self.close()
            
        else:
            #create new task
            t=self.ui.taskName.text()
            priority=int(self.ui.priority.text())
            taskDescription=self.ui.taskDescription.toHtml()
            duedate=self.ui.dueDate.dateTime().toPython().timestamp()
            taskid = self.parent.db.addTask(t,priority,taskDescription, duedate, self.parent.currentContext)
            self.parent.createTaskItem(t, taskid, priority)
            self.parent.adjustHeight()
            self.close()
            
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
                taskname=newdata[:50].strip()
                taskname=taskname.replace("\r\n","\n")
                taskname=taskname.replace("\n"," ")
                taskname=taskname.replace("\t"," ")
                taskname=taskname.replace("  ","")
                taskname=taskname[:20]+"..."
                taskDescription=newdata
                self.ui.taskInput.setText(taskname)
                self.addTask(taskDescription)
            else:
                taskname=fulldata
                taskDescription=""
                self.ui.taskInput.setText(taskname)
                self.addTask(taskDescription)

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
        f=QtGui.QFont()
        f.setFamily(fontName)
        f.setPointSize(fontSize)
        
        if self.ui.editorBold.isFlat():
            f.setBold(True)
        else:
            pass
        
        if self.ui.editorItalic.isFlat():
            f.setItalic(True)
        else:
            pass
        
        if self.ui.editorUnderline.isFlat():
            f.setUnderline(True)
        else:
            pass
        
        if selection.hasSelection():
            Editor.setCurrentFont(f)
            Editor.setFocus()
        else:
            Editor.setCurrentFont(f)
            Editor.setFocus()
      
    def setFontBold(self):
        
        if not self.ui.editorBold.isFlat():
            self.ui.editorBold.setFlat(True)
            self.setEditorFont()
        else:
            self.ui.editorBold.setFlat(False)
            self.setEditorFont()
   
    def setFontItalic(self):
        if not self.ui.editorItalic.isFlat():
            self.ui.editorItalic.setFlat(True)
            self.setEditorFont()
        else:
            self.ui.editorItalic.setFlat(False)
            self.setEditorFont()
            
    def setFontUnderline(self):
        if not self.ui.editorUnderline.isFlat():
            self.ui.editorUnderline.setFlat(True)
            self.setEditorFont()
        else:
            self.ui.editorUnderline.setFlat(False)
            self.setEditorFont()
    
    def setBGcolor(self):
        currentColor=self.ui.currentBGcolor.palette().button().color()
        newColor=QtGui.QColorDialog.getColor(parent=self.parent)
        if newColor!=QtGui.QColor():
            self.ui.taskDescription.setTextBackgroundColor(newColor)
            self.ui.currentBGcolor.setPalette(newColor)
        else:
            self.ui.currentBGcolor.setPalette(currentColor)
        
    def setTextColor(self):
        currentColor=self.ui.currentTextColor.palette().button().color()
        newColor=QtGui.QColorDialog.getColor(parent=self.parent)
        if newColor!=QtGui.QColor():
            self.ui.taskDescription.setTextColor(newColor)
            self.ui.currentTextColor.setPalette(newColor)
        else:
            self.ui.currentTextColor.setPalette(currentColor)
            
    def setCurrentBGcolor(self):
        color=self.ui.currentBGcolor.palette().button().color()
        self.ui.taskDescription.setTextBackgroundColor(color)
    
    def setCurrentTextColor(self):
        color=self.ui.currentTextColor.palette().button().color()
        self.ui.taskDescription.setTextColor(color)
    