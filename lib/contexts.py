from PySide import QtGui
def loadContexts(self):
        self.contexts={}
        self.ui.menuContext.clear()
        c=0
        for i in self.db.getContexts():
            item=QtGui.QAction(self.ui.menuContext)
            item.setText(i[1])
            item.setCheckable(True)
            item.triggered.connect(lambda item=item,s=self: switchContext(s,item))
            item.setData(i[0])
            self.contexts[i[1]]=i[0]
            if c<10:
                if c==9:
                    item.setShortcut("Ctrl+0")
                else:
                    item.setShortcut("Ctrl+"+str(c+1))
            c+=1
            #item.triggered.connect(self.switchContext)
            self.ui.menuContext.addAction(item)
        self.ui.menuContext.addSeparator()
        nc = QtGui.QAction(self.ui.menuContext)
        nc.setText(QtGui.QApplication.translate("ui","Create new context"))
        nc.triggered.connect(lambda s=self:addContext(s))
        nc.setShortcut("Ctrl+Shift+C")
        self.ui.menuContext.addAction(nc)
        rc = QtGui.QAction(self.ui.menuContext)
        rc.setText(QtGui.QApplication.translate("ui","Remove current context"))
        rc.setShortcut("Ctrl+Shift+X")
        rc.triggered.connect(lambda s=self:removeContext(s))
        self.ui.menuContext.addAction(rc)
        
        
def switchContext(self,item):
    if item.isChecked():
        for i in self.ui.menuContext.children():
            if i!=item and i!=self.ui.menuContext.children()[0]:
                i.setChecked(False)
        self.currentContext=self.contexts[str(item.text())]
        self.loadTasksList()
        self.ui.menuContext.setTitle(item.text())
    else:
        item.setChecked(True)
        
        
def addContext(self):
    ok=False
    dialog=QtGui.QInputDialog.getText(self,QtGui.QApplication.translate("ui","New Context"),QtGui.QApplication.translate("ui","Please enter new context name"),QtGui.QLineEdit.Normal,"",ok)
    if dialog[0] and dialog[1]:
        newid=self.db.addContext(str(dialog[0]))
        self.currentContext=newid
        self.loadTasksList()
        loadContexts(self)
        selectCurrentContext(self)
        
def removeContext(self):
    if len(self.contexts)==1:
        QtGui.QMessageBox.critical(self,QtGui.QApplication.translate("ui","Error"),QtGui.QApplication.translate("ui","Can't remove last context"))
    else:
        if len(self.db.getTasks(self.currentContext))>0:
            QtGui.QMessageBox.critical(self,QtGui.QApplication.translate("ui","Error"),QtGui.QApplication.translate("ui","Can't remove context with active tasks"))
            return False
        if self.questionPopup(QtGui.QApplication.translate("ui","Remove context"), QtGui.QApplication.translate("ui","Do you really want to remove active context?")):
            self.db.deleteContext(self.currentContext)
            self.currentContext=self.db.getContexts()[0][0] 
            self.loadTasksList()
            loadContexts(self)
            selectCurrentContext(self)
            
def selectCurrentContext(self):
    for i in self.ui.menuContext.children():
        if i.data()==self.currentContext:
            i.setChecked(True)
            self.ui.menuContext.setTitle(i.text())
            
        