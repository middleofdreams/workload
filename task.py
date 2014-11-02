from PySide import QtGui, QtCore
from ui.task_ui import Ui_Dialog
from _datetime import datetime


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
        #priority=self.ui.priority.text()
        
        self.ui.priority.valueChanged.connect(self.setPriorityText)
        self.task=self.parent.db.getTaskDetails(taskid)
        if self.task:
            self.setWindowTitle(self.task["name"])
            self.ui.taskName.setText(self.task["name"])
            self.ui.priority.setValue(self.task["priority"])
            self.setPriorityText(self.task["priority"])
            self.ui.createDate.setText(self.task["created"])
            self.ui.taskDescription.setText(self.task["taskdescription"])
            self.ui.closeDate.setText(self.task["closedat"])
            self.ui.dueDate.setDate(self.task["closedat"])
            #DD,MM,YY=self.task["due"].split(".")
            #YYYY,HHmm=YY.split(" ")
            #HH,mm=HHmm.split(":")
            #self.ui.dueDate.setDateTime(QtCore.QDateTime(int(YYYY),int(MM),int(DD),int(HH),int(mm),0,0))
        
        else:
            self.setWindowTitle("Create New Task")
            self.ui.taskName.setText("Enter task name here")
            self.setPriorityText(0)
            #print(QtCore.QDateTime(QtCore.QDate.currentDate()))
            self.ui.dueDate.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate()))
#TODO Automatically set dueDate to: today+2 weeks
        self.move(self.parent.pos())

        r=self.exec_()
        parent.taskOpened=False
        
    def setPriorityText(self,priority):
        priorities=["Not set!","Now","Next","Later","Someday","Awaiting"]
        self.ui.priorityText.setText(priorities[priority])
        

    def closeEvent(self,e):
        print(e)
        
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
        if self.taskid!=0:    
            print ("save task details",taskid)
            taskDescription=self.ui.taskDescription.toPlainText()
            priority=int(self.ui.priority.text())
            taskname=self.ui.taskName.text()
            duedate=self.ui.dueDate.text()
            self.parent.db.setTaskDetails(taskid,taskDescription,priority,taskname,duedate)
            self.updateItem(taskname, priority)
            self.close()
            
        else:
            print ("create new task")
            t=self.ui.taskName.text()
            priority=int(self.ui.priority.text())
            taskDescription=self.ui.taskDescription.toPlainText()
            self.parent.createTaskItem(t, taskid, priority)
            self.parent.adjustHeight()
            taskid = self.parent.db.addTask(t,priority,self.parent.currentContext)
            self.close()
