from PySide import QtGui, QtCore
from ui.task_ui import Ui_Dialog



class Task(QtGui.QDialog):

    def __init__(self,parent,taskid):
        '''main window init'''
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint
                            | QtCore.Qt.WindowStaysOnTopHint)
        self.parent=parent
        self.task=self.parent.db.getTaskDetails(taskid)
        self.setWindowTitle(self.task["name"])
        self.ui.taskName.setText(self.task["name"])
        self.ui.priority.setValue(self.task["priority"])
        self.setPriorityText(self.task["priority"])
        
        self.exec_()
        
    def setPriorityText(self,priority):
        priorities=["Not set!","Now","Next","Later","Someday","Awaiting"]
        self.ui.priorityText.setText(priorities[priority])