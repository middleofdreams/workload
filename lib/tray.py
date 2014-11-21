from PySide import QtGui
import os

class Trayicon(QtGui.QSystemTrayIcon):
    def __init__(self,parent=None):
        QtGui.QSystemTrayIcon.__init__(self,parent)
        self.parent=parent
        icon=QtGui.QIcon(':/icon/icon.png')
        self.setIcon(icon)
        self.show()
        self.activated.connect(self.showApp)
        self.iconMenu = QtGui.QMenu(parent)
        self.setContextMenu(self.iconMenu)
        add=self.iconMenu.addAction(self.tr("Create task"))
        add.triggered.connect(self.createTask)
      
        self.iconMenu.addSeparator()
        exitAction=self.iconMenu.addAction(self.tr("Exit"))
        exitAction.triggered.connect(self.exit)
        self.messageClicked.connect(self.parent.show)
       
        
    def showApp(self,reason):
        if reason==QtGui.QSystemTrayIcon.ActivationReason.Trigger:
            if self.parent.isVisible():
                self.parent.hide()
            else:
                self.parent.show()
                
    def createTask(self):
        self.parent.createTask()
        self.show()
        
    def exit(self):
        self.parent.show()
        self.parent.exit()

 