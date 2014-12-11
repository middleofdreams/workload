import time,datetime,codecs
from PySide import QtGui

def export(tasks,filename,dateformat):
    editor=QtGui.QTextBrowser()
    columns=['taskname','created','priority','due','closed','closedat','taskdescription']
    out=""
    for i in tasks:
        for attr in range(len(columns)):
            plainDesc=""
            if attr==6:
                desc=i[attr]
                editor.selectAll()
                editor.insertHtml(desc)
                plainDesc=editor.toPlainText()
                plainDesc=plainDesc.replace("\r\n","\n")
                if len(plainDesc.strip())!=0:
                    out+="taskdescription:"+plainDesc.rstrip()+"\n"
                out+="\n\n"
            else:
                if attr==1 or attr==3 or attr==5:
                    try:
                        timestamp=int(i[attr].split(".")[0])
                        date=datetime.datetime.fromtimestamp(timestamp)
                        date=date.strftime(dateformat)
                    except AttributeError:
                        date=None
                    if date is not None:
                        out+=columns[attr]+":"+str(date)+"\n"
                else:
                    if attr==4:
                        if i[attr]==0:
                            pass
                        else:
                            out+=columns[attr]+":"+str(i[attr])+"\n"
                    else:
                        if len(str(i[attr]).strip())!=0:
                            out+=columns[attr]+":"+str(i[attr])+"\n"
                        else:
                            pass
                
    f=codecs.open(filename,'w','utf-8')
    f.write(out.rstrip())
    f.close()
    
def doAction(self,taskdata,dateformat):
    if self.checkIfExist(taskdata["taskname"]) is not True:
        try:
            desc=taskdata["taskdescription"].rstrip("<br />")
            desc="<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\"></style></head><body>"+desc+"</body></html>"
        except KeyError:
            desc=""
        try:
            duedate=time.mktime(time.strptime(taskdata["due"].strip(),dateformat))
        except KeyError:
            duedate=None
        try:
            priority=taskdata["priority"]
        except KeyError:
            priority=0
        taskid = self.db.addTask(taskdata["taskname"],priority,desc,duedate, self.currentContext)
        self.createTaskItem(taskdata["taskname"], taskid, int(priority))
        self.adjustHeight()
        self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","Import finished."),3300)
    else:
        msg="cannot import task: "+taskdata["taskname"].strip()+", task with same name already exist"
        self.showMsg(msg)
    
def importTasks(self,filename,dateformat):
    f=codecs.open(filename,'r','utf-8')
    input=f.read()
    f.close()
    columns=['taskname','taskdescription','priority','due',]
    ignoreColumns=['closed','closedat','created']    
    allLines=len(input.splitlines()) 
    lasttask={}
    self.attr=""
    taskdata={}
    line=0
    l=0
    for i in input.splitlines():
        line+=1
        i=i.replace("<","&#60;")
        i=i.replace(">","&#62;")
        if "taskname:" in i:
            lasttask=taskdata
            if self.attr!="":
                doAction(self,lasttask,dateformat)
            else:
                taskdata={}
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
        if line==allLines:
             doAction(self,taskdata,dateformat)
