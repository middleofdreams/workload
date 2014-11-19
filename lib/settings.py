class Settings(dict):
    def __init__(self,parent):
        dict.__init__(self)
        self.parent=parent
        self.db=parent.db
        self.__defaults={"notifyOnlyCurrentContext":False,
                         "askOnExit":True,
                         "notifyTime":"300",
                         "notifyInterval":"30",
                         "dateFormat":"%d-%m-%Y %H:%M",
                         "defaultDueDateOn":True,
                         "defaultDueDateValue":"24",
                         "defaultDueDateUnit":"0",
                         "chosenFonts":"Monospace",
                         "mainWindowOpacity":"90",
                         "taskWindowOpacity":"90",
                         "tasklistFont":"Monospace",
                         "tasklistFontSize":"8",
                         "tasklistFontColor":"(0,0,0,255)",
                         "windowBG":"(219,237,255)",
                         "taskEditorBG":"(219,237,255)",
                         "taskEditorFrame":"(0,0,0)",
                         "windowFrame":"(85,170,255)",
                         "tasklistBG":"(219,237,255)",
                         "tasklistFrame":"(85,170,255)",
                         "alternateListItem":"(170,213,255)",
                         "selectedMenuItem":"(170,213,255)",
                         "keyMainWindowToggle":"Ctrl+Space"
        }
                            
        self.__booleans=["notifyCurrentContext","askOnExit","showNotifications","defaultDueDateOn"]
        
    def __getitem__(self,key):
        setting=self.db.getSetting(key)
        if setting is None:
            try:
                setting=self.__defaults[key]
            except:
                pass
        if key in self.__booleans:
            if setting=="0":
                setting=False
            else:
                setting=True
        return setting
    
    def __setitem__(self,key,value):
        self.db.setSetting(key,value)

        
    def getInitContext(self):
        contexts=list(self.parent.contexts.values())
        c=self.db.getSetting("loadContext")
        if c=="last" or c is None:
            try:
                c=int(self.db.getSetting("lastContext"))
            except TypeError:
                c=-1
        else:
            c=int(c)
        if int(c) not in contexts:
            c=contexts[0]
        return c
    
    
 
    def setLastContext(self,context):
        self.db.setSetting("lastContext",context)
        
    def setLoadContext(self,context):
        self.db.setSetting("loadContext", context)
        
    def setCurrentContextAsLast(self):
        self.setLastContext(self.parent.currentContext)
