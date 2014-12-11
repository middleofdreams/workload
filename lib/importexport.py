import time,datetime,codecs
from PySide import QtGui
def export(tasks,filename,dateformat):
    editor=QtGui.QTextBrowser()
    columns=['taskname','taskdescription','created','priority','due','closed','closedat']
    out=""
    for i in tasks:
        for attr in range(len(columns)):
            plainDesc=""
            if attr==1:
                editor.selectAll()
                editor.insertHtml(i[attr])
                plainDesc=editor.toPlainText()
                out+="taskdescription:"+plainDesc.rstrip("\n")+"\n"
            else:
                if attr==2 or attr==4 or attr==6:
                    try:
                        timestamp=int(i[attr].split(".")[0])
                        date=datetime.datetime.fromtimestamp(timestamp)
                        date=date.strftime(dateformat)
                    except AttributeError:
                        date=None
                    out+=columns[attr]+":"+str(date)+"\n"
                else:
                    if len(str(i[attr]).strip())!=0:
                        out+=columns[attr]+":"+str(i[attr])+"\n"
                    else:
                        print("empty line")
            if attr==6:
                out+="\n\n"

    f=codecs.open(filename,'w','utf-8')
    f.write(out)
    f.close()
    
def importTasks(self,filename,dateformat):
    f=codecs.open(filename,'r','utf-8')
    input=f.read()
    f.close()
    columns=['taskname','taskdescription','priority','due',]
    ignoreColumns=['closed','closedat','created']
    task=False              
    taskdata={}
    self.attr=""
    line=1
    for i in input.splitlines():
        line+=1
        if task==True or "taskname:" in i:
            task=True
            if i.strip()=="":
                l+=1
            if ":" in i or len(i.strip())!=0:
                l=0
                attr=i.split(":")[0]
                if attr not in ignoreColumns:
                    if attr not in columns:
                        v+=i+"<br /> "
                        attr=self.attr
                    else:
                        if attr=="taskdescription":
                            v=i[len(attr)+1:]+"<br />"
                        else:
                            v=i[len(attr)+1:]
                        self.attr=attr
                    taskdata[self.attr]=v
                else:
                    pass
            else:
                if self.attr=="taskdescription":
                    v+="<br />"
                    taskdata[self.attr]=v
                    l=0
                else:
                    l+=1
            if l==2:
                task=False
                self.attr=""
                if len(taskdata.keys())>=3:
                    try:
                        desc=taskdata["taskdescription"]
                        desc="<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\"></style></head><body>"+desc+"</body></html>"
                        taskdata["taskdescription"]=desc
                    except KeyError:
                        taskdata["taskdescription"]=""
                    if self.checkIfExist(taskdata["taskname"]) is not True:
                        duedate=time.mktime(time.strptime(taskdata["due"].strip(),dateformat))
                        taskid = self.db.addTask(taskdata["taskname"],taskdata["priority"], taskdata["taskdescription"],duedate, self.currentContext)
                        self.createTaskItem(taskdata["taskname"], taskid, int(taskdata["priority"]))
                        self.adjustHeight()
                        self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","Import finished."),3300)
                    else:
                        msg="cannot import task: "+taskdata["taskname"].strip()+", task with same name already exist"
                        self.showMsg(msg)
                else:
                    msg="cannot import task:\""+taskdata["taskname"].strip()+"\", task attributes are missing.\n (line: "+str(line-2)+")"
                    self.showMsg(msg)
                taskdata={}