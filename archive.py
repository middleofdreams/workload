from PySide import QtGui,QtCore
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
        
        self.ui.nameFilter.textChanged.connect(self.filter)
        self.ui.contextFilter.textChanged.connect(self.filter)
        self.ui.createFilter.textChanged.connect(self.filter)
        self.ui.closeFilter.textChanged.connect(self.filter)
        
        self.ui.treeWidget.setFocus()

        self.exec_()
        
        
    def openTask(self,item):
        Task(self.parent,item.data(0, 32))
        
    def keyPressEvent(self,e):
        if e.key()==16777216:
            self.ui.nameFilter.clear()
            self.ui.contextFilter.clear()
            self.ui.createFilter.clear()
            self.ui.closeFilter.clear()
        

    def filter(self,t):
        filters=[self.ui.nameFilter.text(),self.ui.contextFilter.text(),self.ui.createFilter.text(),self.ui.closeFilter.text() ]
        for item in (self.ui.treeWidget.findItems("", QtCore.Qt.MatchContains|QtCore.Qt.MatchRecursive)):
            item.setHidden(False)
        for filterText in filters:
            if len(filterText)>2:
                allitems=[]
                for item in self.ui.treeWidget.findItems("", QtCore.Qt.MatchContains|QtCore.Qt.MatchRecursive):
                    if not item.isHidden():
                        allitems.append(item)
                allitems=set(allitems)
                for item in self.ui.treeWidget.findItems(filterText, QtCore.Qt.MatchContains,filters.index(filterText)):
                        try:
                            allitems.remove(item)
                        except KeyError:
                                pass
                for item in allitems:
                    item.setHidden(True)
                    
            
                    
        
      
        