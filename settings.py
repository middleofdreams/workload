class Settings(object):
    def __init__(self,parent):
        self.parent=parent
        self.db=parent.db
        
    def getInitContext(self):
        contexts=list(self.parent.contexts.values())
        c=self.db.getSetting("loadContext")
        if c=="last" or c==None:
            c =int(self.db.getSetting("lastContext"))
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