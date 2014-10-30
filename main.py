# -*- coding: utf-8 -*-

from PySide import QtGui,QtCore
from ui.main_ui import Ui_MainWindow
from db import DB

class Workload(QtGui.QMainWindow):
    def __init__(self):
        '''main window init'''
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
        
        desktop=QtGui.QApplication.desktop()

        self.move(10,(desktop.height()/2)-(self.height()))
        
        self.show()
        k = QtGui.QShortcut(self)
        k.setKey("Return")
        k.activated.connect(self.addTask)
        k = QtGui.QShortcut(self)
        k.setKey("Enter")
        k.activated.connect(self.addTask)
        self.ui.taskList.setColumnWidth(0,20)           #zmieniona szerokość pierwszej kolumny
        
        self.currentContext=1 #tymczasowo
        
        self.db=DB(self)
        self.loadTasksList()

        
        
    def addTask(self):
        t=self.ui.taskInput.text()
        self.ui.taskInput.clear()
        taskid=self.db.addTask(str(t))
        self.createTaskItem(t, taskid)

        
    def createTaskItem(self,t,id=None):                 #trzeba rozszerzyc o priorytet
        item=QtGui.QTreeWidgetItem(["",t])
        item.setSizeHint(0, QtCore.QSize(0,22))         #zmieniona wysokość wiersza
        self.ui.taskList.addTopLevelItem(item)
        
        backColor = QtGui.QColor("#ff0000")                 #kolor tła kolumny (priorytet dla elementu)
        item.setBackground(0, backColor)                #jak teraz juz tylko jakas funkcje na kolorowanie priorytetow i bedzie git : )
        
                                                        #z takich wizualnych rzeczy mozna dorobic jakas cienka ramke dookola okna.. bo na bialym tle sie to gubi;p
        
                                                
                                                
                                                
                                                #teraz na takie cos wpadlem: jesli wkleisz do inputu tekst wiekszy niz>x to 
                                                #otworzy sie to okienko podgladu zadania, bedzie mozna podejrzec cala tresc
                                                #zadania i ustalic poprawny naglowek/tytul
                                                
                                                
    def loadTasksList(self,archived=False):
        for i in self.db.getTasks(self.currentContext):
            self.createTaskItem(i[1], i[0])
                                                
                                                
                                                
                                                
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myapp = Workload()

    res=app.exec_()
    sys.exit()
