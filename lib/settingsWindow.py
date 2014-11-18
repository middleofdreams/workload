from PySide import QtCore,QtGui
from ui.settings_ui import Ui_Dialog

class SettingsWindow(QtGui.QDialog):

    def __init__(self,parent):
        '''settings window init'''
        self.parent=parent
        self.settings=parent.settings
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        ## CONNECT SIGNALS
        self.ui.windowBG.clicked.connect(self.getWindowBGcolor)
#         self.ui.windowFrame.clicked.connect(self.updateStyle)
#         self.ui.tasklistBG.clicked.connect(self.updateStyle)
#         self.ui.tasklistFrame.clicked.connect(self.updateStyle)
#         self.ui.tasklistFontColor.clicked.connect(self.updateStyle)
#         self.ui.taskEditorBG.clicked.connect(self.updateStyle)
        
        self.ui.notificationsOn.stateChanged.connect(self.notificationsSwitch)
        self.ui.defaultDueTimeOn.stateChanged.connect(self.defaultDueSwitch)
        self.ui.notifyIntervalUnit.currentIndexChanged.connect(lambda e:self.setSpinMax(e, self.ui.notifyIntervalSpin, [600, 60]))
        self.ui.notifyTimeUnit.currentIndexChanged.connect(lambda e:self.setSpinMax(e, self.ui.notifyTimeSpin, [600, 60]))
        self.ui.defaultDueTimeUnit.currentIndexChanged.connect(lambda e:self.setSpinMax(e, self.ui.defaultDueTimeSpin, [24, 60]))
        self.ui.windowOpacity.valueChanged.connect(self.editWindowOpacity)
        self.ui.tasklistFont.activated.connect(self.editTasklistFont)
        self.ui.tasklistFontSize.valueChanged.connect(self.editTasklistFont)
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
            
        self.ui.confirmExit.setChecked(self.settings["askOnExit"])
        
        self.ui.dateFormat.setText(self.settings["dateFormat"])
        
        notifyTime=int(self.settings["notifyTime"])
        if notifyTime>60:
            notifyTime/=60
            self.ui.notifyTimeUnit.setCurrentIndex(0)
        else:
            self.ui.notifyTimeUnit.setCurrentIndex(1)
        self.ui.notifyTimeSpin.setValue(notifyTime)
        
        notifyInterval=int(self.settings["notifyInterval"])
        
        
        if notifyInterval>60:
            notifyInterval/=60
            self.ui.notifyIntervalUnit.setCurrentIndex(0)
        else:
            self.ui.notifyIntervalUnit.setCurrentIndex(1)
        self.ui.notifyIntervalSpin.setValue(notifyInterval)
        
        self.ui.notificationsOn.setChecked(self.settings["showNotifications"])
        
        self.ui.notificationsCurrentContext.setChecked(self.settings["notifyCurrentContext"])
        self.ui.defaultDueTimeOn.setChecked(self.settings["defaultDueDateOn"])
        self.ui.defaultDueTimeSpin.setValue(int(self.settings["defaultDueDateValue"]))
        self.ui.defaultDueTimeUnit.setCurrentIndex(int(self.settings["defaultDueDateUnit"]))
        
        self.loadFontList()
        self.ui.windowOpacity.setValue(int(self.settings["mainWindowOpacity"]))
        self.ui.taskEditorOpacity.setValue(int(self.settings["taskWindowOpacity"]))
        currentIndex=self.ui.tasklistFont.findText(self.settings["tasklistFont"])
        self.ui.tasklistFont.setCurrentIndex(currentIndex)
        self.ui.tasklistFontSize.setValue(int(self.settings["tasklistFontSize"]))
        self.ui.addFonts.clicked.connect(self.addFonts)
        self.ui.removeFonts.clicked.connect(self.removeFonts)
        if self.exec_():
            #save load context values
            r=self.ui.startupContext.currentIndex()
            if r==0:
                self.settings.setLoadContext("last")
            else:
                context=self.ui.startupContext.itemData(r)
                self.settings.setLoadContext(context)
            #save current context in db (just in case)
            self.settings.setCurrentContextAsLast()
            
            #save notify times
            notifyTime=int(self.ui.notifyTimeSpin.value())
            if self.ui.notifyTimeUnit.currentIndex()==0:
                notifyTime*=60
            self.settings['notifyTime']=notifyTime
            
            notifyInterval=int(self.ui.notifyIntervalSpin.value())
            if self.ui.notifyIntervalUnit.currentIndex()==0:
                notifyInterval*=60
            self.settings["notifyInterval"]=notifyInterval
            
            # save askOnExit
            self.settings["askOnExit"]=self.ui.confirmExit.isChecked()
            # save dateformat
            self.settings["dateFormat"]=str(self.ui.dateFormat.text())
            # save notify on
            self.settings["showNotifications"]=self.ui.notificationsOn.isChecked() 
            #save notify current context
            self.settings["notifyCurrentContext"]=self.ui.notificationsCurrentContext.isChecked()
            #save default due date
            self.settings["defaultDueDateOn"]=self.ui.defaultDueTimeOn.isChecked()
            self.settings["defaultDueDateValue"]=self.ui.defaultDueTimeSpin.value()
            self.settings["defaultDueDateUnit"]=self.ui.defaultDueTimeUnit.currentIndex()
            #save chosen fonts
            self.saveChosenFonts()
            #save opacity settings
            self.editWindowOpacity(save=True)
            #save tasklist font settings
            self.editTasklistFont(save=True)
         
    def getWindowBGcolor(self):
        currentColor=self.settings["windowBGcolor"]
        newColor=QtGui.QColorDialog.getColor(parent=self.parent)
        if newColor!=QtGui.QColor():
            self.setButtonColor(self.ui.windowBG, newColor.getRgb())
            self.settings["windowBGcolor"]=str(newColor.getRgb())
        else:
            self.setButtonColor(self.ui.windowBG, currentColor)
   
    def setButtonColor(self,button,color):
        style="QPushButton[Button=settings] {height: 15px; border: 1px solid rgba(0, 0, 0,190);  border-radius: 2px;border-style: outset; background-color:rgba"+str(color)+"}"
        button.setProperty('Button','settings')    
        button.setStyleSheet(style)
        
    
    def editTasklistFont(self,save=False):
        font=QtGui.QFont(self.ui.tasklistFont.currentText())
        font.setPointSize(self.ui.tasklistFontSize.value())
        self.parent.ui.taskList.setFont(font)
        if save:
            self.settings["tasklistFont"]=self.ui.tasklistFont.currentText()
            self.settings["tasklistFontSize"]=self.ui.tasklistFontSize.value()
    
    def editWindowOpacity(self,save=False):
        windowOpacity=self.ui.windowOpacity.value()
        taskEditorOpacity=self.ui.taskEditorOpacity.value()
        self.parent.setWindowOpacity(int(windowOpacity)/100)
        
        if save:
            self.settings["mainWindowOpacity"]=windowOpacity
            self.settings["taskWindowOpacity"]=taskEditorOpacity
            
    def notificationsSwitch(self,e):
        if e==2:
            disable=False
        else:
            disable=True
           
        self.ui.notificationsCurrentContext.setDisabled(disable)
        self.ui.notifyIntervalSpin.setDisabled(disable)
        self.ui.notifyIntervalUnit.setDisabled(disable)
        self.ui.notifyTimeSpin.setDisabled(disable)
        self.ui.notifyTimeUnit.setDisabled(disable)
        
    def loadFontList(self):
        FontDB=QtGui.QFontDatabase()
        allFonts=FontDB.families()
        for i in allFonts:
            self.ui.allFonts.addItem(i)
        
        chosenFonts=self.settings["chosenFonts"].split("|")
        for i in chosenFonts:
            self.ui.chosenFonts.addItem(i)
            self.ui.tasklistFont.addItem(i)
            
            
        
    def addFonts(self):
        selectedFonts=self.ui.allFonts.selectedItems()
        for i in selectedFonts:
            self.ui.chosenFonts.addItem(i.text())
        
        
    def removeFonts(self):
        selectedFonts=self.ui.chosenFonts.selectedItems()
        for i in selectedFonts:
            item=self.ui.chosenFonts.row(i)
            self.ui.chosenFonts.takeItem(item)
    
    def saveChosenFonts(self):
    
        allItems=self.ui.chosenFonts.findItems("",QtCore.Qt.MatchFlags(QtCore.Qt.MatchContains|QtCore.Qt.MatchRecursive))
        allFonts=[]
        for i in allItems:
            allFonts.append(i.text())
        self.settings["chosenFonts"]="|".join(allFonts)
    
    
    def defaultDueSwitch(self,e):
        if e==2:
            disable=False
        else:
            disable=True
        self.ui.defaultDueTimeSpin.setDisabled(disable)
        self.ui.defaultDueTimeUnit.setDisabled(disable)
        
    def setSpinMax(self,e,spinobject,maxValues):
        spinobject.setMaximum(maxValues[e])
            