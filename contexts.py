from PySide import QtGui
def loadContexts(self):
        self.contexts={}
        self.ui.menuContext.clear()
        
        for i in self.db.getContexts():
            item=QtGui.QAction(self.ui.menuContext)
            item.setText(i[1])
            item.setCheckable(True)
            item.triggered.connect(lambda item=item,s=self: switchContext(s,item))
            item.setData(i[0])
            self.contexts[i[1]]=i[0]
            #item.triggered.connect(self.switchContext)
            self.ui.menuContext.addAction(item)
        self.ui.menuContext.addSeparator()
        nc = QtGui.QAction(self.ui.menuContext)
        nc.setText("Create new context")
        nc.triggered.connect(lambda s=self:addContext(s))
        self.ui.menuContext.addAction(nc)
        rc = QtGui.QAction(self.ui.menuContext)
        rc.setText("Remove current context")
        rc.triggered.connect(lambda s=self:removeContext(s))
        self.ui.menuContext.addAction(rc)
        
        
def switchContext(self,item):
    if item.isChecked():
        for i in self.ui.menuContext.children():
            if i!=item and i!=self.ui.menuContext.children()[0]:
                i.setChecked(False)
        self.currentContext=self.contexts[str(item.text())]
        self.db.setSetting("lastContext",self.currentContext)
        self.loadTasksList()
    else:
        item.setChecked(True)
        
        
def addContext(self):
    ok=False
    dialog=QtGui.QInputDialog.getText(self,"New Context","Please enter new context name",QtGui.QLineEdit.Normal,"",ok)
    if dialog[0] and dialog[1]:
        self.db.addContext(str(dialog[0]))
        loadContexts(self)
        
def removeContext(self):
    if self.currentContext==1:
        QtGui.QMessageBox.critical(self,"Error","Removal of first context is not possible atm. TBD later")
#TODO: some settings table with saved last opened context
    else:
        if len(self.db.getTasks(self.currentContext))>0:
            QtGui.QMessageBox.critical(self,"Error","Can't remove context with active tasks")
            return False
        if self.questionPopup("Remove context", "Do you really want to remove active context?"):
            self.db.deleteContext(self.currentContext)
            self.currentContext=1 #TODO: change it to first available
            self.loadTasksList()
            loadContexts(self)
            
def selectCurrentContext(self):
    for i in self.ui.menuContext.children():
        if i.data()==self.currentContext:
            i.setChecked(True)
        