import sqlite3,datetime
class DB(object):
    def __init__(self,parent):
        self.parent=parent
        #self.start()
        self.db=sqlite3.connect("workload.db")
        self.c=self.db.cursor()
        
    def addTask(self,taskname,taskpriority=5,context=1):
        now=datetime.datetime.now().isoformat()
        t=(taskname,taskpriority,context,now)
        self.c.execute("INSERT into tasks ('taskname', 'priority','context','created') values (?,?,?,?)",t)
        self.db.commit()
        for i in self.c.execute("SELECT last_insert_rowid()"):
            return i[0]
        
        
    def getTasks(self,context):
        t=(context,)
        tasks=[]
        for i in self.c.execute("SELECT rowid,taskname,priority FROM tasks where context=?",t): tasks.append(i)
        return tasks
    
    def deleteTask(self,taskid):
        t=(taskid,)
        self.c.execute("Delete from tasks where rowid=?",t)
        self.db.commit()
        print(taskid)