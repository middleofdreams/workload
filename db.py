import sqlite3
import datetime


class DB(object):
    def __init__(self, parent):
        self.parent = parent
        #self.start()
        self.db = sqlite3.connect("workload.db")
        self.c = self.db.cursor()
        self.checkDB()

    def addTask(self, taskname, priority, taskDescription, duedate, context=1):
        now = datetime.datetime.now().timestamp()
        t = (taskname, priority, taskDescription, duedate, context, now)
        self.c.execute("INSERT into tasks ('taskname','priority','taskdescription','due','context',\
            'created','closed') values (?,?,?,?,?,?,0)", t)
        self.db.commit()
        for i in self.c.execute("SELECT last_insert_rowid()"):
            return i[0]

    def getTasks(self, context,archive=False):
        if archive: archive=1
        else:archive=0
        t = (context,archive)
        tasks = []
        for i in self.c.execute("SELECT rowid,taskname,priority \
            FROM tasks where context=? and closed=?", t):
            tasks.append(i)
        return tasks

    def deleteTask(self, taskid):
        t = (taskid, )
        self.c.execute("Delete from tasks where rowid=?", t)
        self.db.commit()
        
    def setTaskPriority(self,taskid,priority):
        t = (priority, taskid)
        self.c.execute("Update tasks set priority=? where rowid=?", t)
        self.db.commit()
     
    def getTaskDetails(self,taskid):
        t = (taskid,)
        for i in self.c.execute("SELECT * from tasks where rowid=?", t):
            columns=["name","taskdescription","created","priority","due","closed","closedat","context"]
            task={}
            for j in range(0,len(i)):
                task[columns[j]]=i[j]
            return task
    
    def setTaskDetails(self,taskid,description,priority,taskname,duedate):
        t = (description,duedate,priority,taskname,taskid)
        self.c.execute("Update tasks set taskdescription=?,due=?,priority=?,taskname=? where rowid=?", t)
        self.db.commit()
        
    def completeTask(self,taskid):
        t = (datetime.datetime.now().timestamp(),taskid)
        self.c.execute("Update tasks set closed=1,closedat=? where rowid=?", t)
        self.db.commit()
        
    def addContext(self,contextname):
        t = (contextname, )
        self.c.execute("INSERT into contexts ('contextname') values (?)", t)
        self.db.commit()
        for i in self.c.execute("SELECT last_insert_rowid()"):
            return i[0]
        
    def deleteContext(self,contextid):
        t = (contextid, )
        self.c.execute("Delete from contexts where rowid=?", t)
        self.db.commit()
        
    def getContexts(self):
        return self.c.execute("SELECT rowid,contextname from contexts order by rowid ASC")


    def checkDB(self):
        try:
            self.c.execute("Select * from tasks limit 1")
        except sqlite3.OperationalError:
            self.createDB()

    def createDB(self):
        query='CREATE TABLE tasks (\
        "taskname" TEXT NOT NULL,\
        "taskdescription" TEXT,\
        "created" TEXT,\
        "priority" INTEGER,\
        "due" TEXT,\
        "closed" BOOL,\
        "closedat" TEXT,\
        "context" INTEGER NOT NULL DEFAULT (1)\
        )'
        self.c.execute(query)
        
        query='CREATE TABLE "contexts" (\
        "contextname" TEXT)'
        self.c.execute(query)
        query="INSERT INTO 'contexts' VALUES ('Default');"
        self.c.execute(query)
        self.db.commit()