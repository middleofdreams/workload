class Settings(object):
    def __init__(self,parent):
        self.parent=parent
        self.db=parent.db
        
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
        
    def getDateFormat(self):
        df=self.db.getSetting("dateFormat")
        if df==None:
            df="%d-%m-%Y %H:%M"
        return df