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
        colorButtons={"windowBG":self.ui.windowBG,"windowFrame":self.ui.windowFrame,"tasklistBG":self.ui.tasklistBG,"tasklistFrame":self.ui.tasklistFrame,"tasklistFontColor":self.ui.tasklistFontColor,"taskEditorBG":self.ui.taskEditorBG}
        for k,v in colorButtons.items():
            v.clicked.connect(lambda button=v,setting=k :self.editStyle(button,setting))

        
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
        
        self.ui.mainWindowToggleKey.setText(self.settings['keyMainWindowToggle'])
        
        
        #kill shortcut handler to be able to grab new shortcut:
        self.parent.shortcuts.terminate()
        self.ui.mainWindowToggleKey.keyPressEvent=self.grabToggleMainWindowKey
        
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
        else:
            self.parent.setWindowOpacity(int(self.settings["mainWindowOpacity"])/100)
            
        self.parent.shortcuts.start()
         
    def editStyle(self,button,setting):
        print(button,setting)
        currentColor=button.palette().button().color()
        newColor=QtGui.QColorDialog.getColor(parent=self.parent)
        if newColor!=QtGui.QColor():
            self.setButtonColor(button, newColor.getRgb())
            print("picked color",str(newColor.getRgb()))
            self.settings[setting]=str(newColor.getRgb())
            
        else:
            self.setButtonColor(button, currentColor)
   
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
    
    def editWindowOpacity(self,v=None,save=False):
        if not v:
            windowOpacity=self.ui.windowOpacity.value()
        else:
            windowOpacity=v
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
        
    def grabToggleMainWindowKey(self, e):
        if self.ui.mainWindowToggleKey.hasFocus():
            if e.text()!="":
                k=""
                if QtCore.Qt.ControlModifier & e.modifiers():
                    k+="Ctrl + "
                if QtCore.Qt.ShiftModifier & e.modifiers():
                    k+="Shift + "
                if QtCore.Qt.AltModifier & e.modifiers():
                    k+="Alt + "
                if k!="":
                    #ne=QtGui.QKeyEvent(e.type(),e.key(),QtCore.Qt.NoModifier)
                    print(e.text())
                    
                    #k+=str(QtCore.QString().number(e.key()))
                    self.ui.mainWindowToggleKey.setText(k)
        
            
