from PySide import QtCore
import datetime
from .helpers import timestamp

class TaskReminder(QtCore.QTimer):
    '''QTimer based class used for notifications'''
    markTasks=QtCore.Signal(list)
    
    def __init__(self,parent):
        '''init function'''
        QtCore.QTimer.__init__(self,parent)
        self.parent=parent
        self.db=parent.db
        self.settings=parent.settings
        self.activeNotifies={}
        self.lastFound={}
        self.timeout.connect(self.getNearEndTasks)
        self.markTasks.connect(self.parent.setMarker)
        self.getNearEndTasks(force=True)
        self.start(60000)
        #self.start(1000)
        
    def getNearEndTasks(self,force=False):
        onlyCurrentContext=self.settings["notifyCurrentContext"]
        notifyInterval=int(self.settings["notifyInterval"])
        notifyTime=int(self.settings["notifyTime"])
        td=datetime.timedelta(minutes=int(notifyTime))
        nt=datetime.datetime.now()+td
        ts=timestamp(nt)
        notify=[]
        foundtasks={}
        for i in self.db.getTasksByTimestamp(ts,onlyCurrentContext):
            foundtasks[i[0]]=[i[1],i[2]]
            if i[0] in self.activeNotifies.keys():
                self.activeNotifies[i[0]]+=1
            else:
                self.activeNotifies[i[0]]=0
                notify.append(i[0])
                
        removeFromActive=[]
        for k,v in self.activeNotifies.items():
            if k not in foundtasks.keys():
                removeFromActive.append(k)
            else:
                if v % notifyInterval==0:
                    notify.append(k)
                    
        for k in removeFromActive:
            del self.activeNotifies[k]
            
        if not force:
            tasks={}
            for i in notify:
                tasks[i]=foundtasks[i]
            if self.settings["showNotifications"]:
                self.showNotification(tasks)
        if self.lastFound!=foundtasks:
            self.markTasks.emit(list(foundtasks.keys()))
        self.lastFound=foundtasks
        
    def showNotification(self,tasks):
        if len(tasks)>0:
            if len(tasks)>1: 
                taskNames=""
                for v in tasks.values():
                    taskNames+="\n"+v[0]+" - "+self.formatDate(v[1])
                msg=self.tr("Following tasks:")+taskNames
            else:
                n,d=list(tasks.values())[0]
                msg=self.tr("Following task:")+"\n"+n+" - "+self.formatDate(d)
            self.parent.tray.showMessage("Workload", msg)
            
        
    def formatDate(self,tmstpm):
        tmstpm=tmstpm.split(".")[0]
        d=datetime.datetime.fromtimestamp(int(tmstpm))
        now=datetime.datetime.now()
        if d.date()==now.date():
            if d<now:
                formatted=self.tr(" already ended!")
            else:
                formatted=self.tr(" ends at ")+d.strftime("%H:%M")
        elif d.date()<now.date():
            formatted=self.tr(" already ended!")
        elif (d.date()-now.date()).days==1:
            formatted=self.tr(" ends tomorrow at")+d.strftime(" %H:%M")
        else:
            formatted=self.tr(" ends")+d.strftime(" %d.%m")+self.tr(" at")+d.strftime(" %H:%M")
            
        return formatted
        
        
        
        
        

        