from PySide import QtCore
import datetime
from .helpers import timestamp

class TaskReminder(QtCore.QTimer):
    '''QTimer based class used for notifications'''
    
    def __init__(self,parent):
        '''init function'''
        QtCore.QTimer.__init__(self,parent)
        self.parent=parent
        self.db=parent.db
        self.settings=parent.settings
        self.activeNotifies={}
        self.timeout.connect(self.onTimeout)
        #self.start(60000)
        self.start(1000)
        
    def onTimeout(self):
        onlyCurrentContext=self.settings.getNotifyOnlyCurrentContext()
        notifyInterval=self.settings.getNotifyInterval()
        notifyTime=self.settings.getNotifyTime()
        td=datetime.timedelta(minutes=notifyTime)
        print (td)
        nt=datetime.datetime.now()+td
        ts=timestamp(nt)
        print(ts)
        notify=[]
        foundtasks={}
        for i in self.db.getTasksByTimestamp(ts,onlyCurrentContext):
            print(i)
            foundtasks[i[0]]=[i[1],i[2]]
            #print(i)
            if i[0] in self.activeNotifies.keys():
                #print("1")
                self.activeNotifies[i[0]]+=1
            else:
                #print("2")
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
        
        tasks={}
        for i in notify:
            tasks[i]=foundtasks[i]
        self.showNotification(tasks)
        
        
    def showNotification(self,tasks):
        if len(tasks)>0:
            if len(tasks)>1:
                taskNames=""
                for v in tasks.values():
                    taskNames+="\n"+v[0]+" - "+self.formatDate(v[1])
                msg="Following tasks:"+taskNames
            else:
                n,d=list(tasks.values())[0]
                msg="Following task:\n"+n+" - "+self.formatDate(d)

            self.parent.tray.showMessage("Workload", msg)
            
        
    def formatDate(self,tmstpm):
        tmstpm=tmstpm.split(".")[0]
        d=datetime.datetime.fromtimestamp(int(tmstpm))
        now=datetime.datetime.now()
        if d.date()==now.date():
            if d<now:
                formatted=" already ended!"
            else:
                formatted=d.strftime(" ends at %H:%M")
        elif d.date()<now.date():
            formatted=" already ended!"
        elif (d.date()-now.date()).days==1:
            formatted=d.strftime(" ends tomorrow at %H:%M")
        else:
            formatted=d.strftime(" ends %d.%m at %H:%M")
            
        return formatted
        
        
        
        
        

        