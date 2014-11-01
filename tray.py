from PySide import QtGui
import os

class Trayicon(QtGui.QSystemTrayIcon):
    def __init__(self,parent=None):
        QtGui.QSystemTrayIcon.__init__(self,parent)
        self.parent=parent
        icon=QtGui.QIcon(os.path.realpath("icon.png"))
        self.setIcon(icon)
        self.show()
        self.activated.connect(self.showApp)
        
    def showApp(self):
        if self.parent.isVisible():
            self.parent.hide()
        else:
            self.parent.show()