from PySide import QtGui
from ui.settings_ui import Ui_Dialog

class SettingsWindow(QtGui.QDialog):

    def __init__(self,parent):
        '''settings window init'''
        self.parent=parent
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        for i in self.parent.db.getContexts():
            self.ui.startupContext.addItem(i[1],i[0])
        
        load=self.parent.db.getSetting("loadContext")
        if load=="last" or load=="":
            self.ui.startupContext.setCurrentIndex(0)
        else:
            try:
                index=self.ui.startupContext.findData(load)
                self.ui.startupContext.setCurrentIndex(index)
            except:
                pass
            
        if self.exec_():
            #save load context values
            r=self.ui.startupContext.currentIndex()
            if r==0:
                self.parent.settings.setLoadContext("last")
            else:
                context=self.ui.startupContext.itemData(r)
                self.parent.settings.setLoadContext(context)
            #save current context in db (just in case)
            self.parent.settings.setCurrentContextAsLast()
            