class Settings(object):
    def __init__(self,parent):
        self.parent=parent
        self.db=parent.db
        
    def getInitContext(self):
        c=self.db.getSetting("loadContext")
        if c=="last" or c==None:
            c =self.db.getSetting("lastContext")
        if c not in self.parent.contexts.values():
            c=list(self.parent.contexts.values())[0]
        print (c)
        return c
        
    def setLastContext(self,context):
        self.db.setSetting("lastContext",context)
    def setLoadContext(self,context):
        self.db.setSetting("loadContext", context)