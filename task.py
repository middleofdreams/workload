from PySide import QtGui, QtCore
from ui.task_ui import Ui_Dialog



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
        
        self.moveIt=False
        self.task=self.parent.db.getTaskDetails(taskid)
        self.setWindowTitle(self.task["name"])
        self.ui.taskName.setText(self.task["name"])
        self.ui.priority.setValue(self.task["priority"])
        self.setPriorityText(self.task["priority"])
        self.ui.createDate.setText(self.task["created"])
        
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
                
