from PySide import QtGui
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
        self.ui.notificationsOn.stateChanged.connect(self.notificationsSwitch)
        self.ui.defaultDueTimeOn.stateChanged.connect(self.defaultDueSwitch)

        self.ui.notifyIntervalUnit.currentIndexChanged.connect(lambda e:self.setSpinMax(e, self.ui.notifyIntervalSpin, [600, 60]))
        self.ui.notifyTimeUnit.currentIndexChanged.connect(lambda e:self.setSpinMax(e, self.ui.notifyTimeSpin, [600, 60]))
        self.ui.defaultDueTimeUnit.currentIndexChanged.connect(lambda e:self.setSpinMax(e, self.ui.defaultDueTimeSpin, [24, 60]))

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
        
    def defaultDueSwitch(self,e):
        if e==2:
            disable=False
        else:
            disable=True
        self.ui.defaultDueTimeSpin.setDisabled(disable)
        self.ui.defaultDueTimeUnit.setDisabled(disable)
        
    def setSpinMax(self,e,spinobject,maxValues):
        spinobject.setMaximum(maxValues[e])
            