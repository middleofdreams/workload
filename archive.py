from PySide import QtGui
from ui.archive_ui import Ui_Dialog
import datetime
from task import Task
class ArchiveWindow(QtGui.QDialog):

    def __init__(self,parent):
        '''settings window init'''
        self.parent=parent
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        contexts={}
        for k,v in self.parent.contexts.items():
            contexts[v]=k
        row=0
        for i in parent.db.getArchive():
            tname=i[1]
            try:
                tcontext=contexts[i[2]]
            except KeyError:
                tcontext=str(i[2])+" [removed]"
            tcontext
            tcreate=datetime.datetime.fromtimestamp(int(i[3].rsplit(".")[0])).strftime("%d-%m-%Y %H:%M")
            tclose=datetime.datetime.fromtimestamp(int(i[4].rsplit(".")[0])).strftime("%d-%m-%Y %H:%M")
            item=QtGui.QTreeWidgetItem([tname,tcontext,tcreate,tclose])
            item.setData(0,32,i[0])
            self.ui.treeWidget.addTopLevelItem(item)
            
        self.ui.treeWidget.itemActivated.connect(self.openTask)
        self.exec_()
        
        
    def openTask(self,item):
        Task(self.parent,item.data(0, 32))