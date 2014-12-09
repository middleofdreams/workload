import time,datetime,codecs
from PySide import QtGui
def export(tasks,filename,dateformat):
    columns=['taskname','taskdescription','created','priority','due','closed','closedat']
    out=""
    for i in tasks:
        for attr in range(len(columns)):
            print (columns[attr],i[attr])
#    out="taskname,taskdescription,created,priority,due,closed,closedat"
#     for i in tasks:
#         ln=""
#         for attr in i:
#             index=i.index(attr)
#             if attr is None:
#                 attr=""
#             if isinstance(attr,int):
#                 attr=bytes(attr).decode()
#             if index==2 or index==4 or index==6:
#                 attr=attr.split(".")[0].strip()
#                 try:
#                     attr=int(attr)
#                 except:
#                     ln+=","
#                     continue
#                 d=datetime.datetime.fromtimestamp(int(attr))
#                 attr=d.strftime(dateformat)
#             attr=attr.replace(",","%comma%")
#             attr=attr.replace("\n","%newline%")
#             attr=attr.replace("\r\n","%newline%")
#             ln+=attr+","
#         out+="\r\n"+ln[:-1]
    f=codecs.open(filename,'w','utf-8')
    f.write(out)
    f.close()
    
def importTasks(self,filename,dateformat):
    filename=filename[0]
    f=codecs.open(filename,'r','utf-8')
    input=f.read()
    f.close()
    columns=['taskname','taskdescription','priority','due',]
    entry=None
    task=False              
    taskdata={}
    tag=0
    l=0
    taskId=0
    self.attr=""
    for i in input.splitlines():
        if "taskname:" in i or task==True:
            self.attr="taskname"
            task=True
            if ":" in i:
                attr=i.split(":")[0]
                if attr not in columns:
                    #print("attribute not in columns, pass line to taskdata:",i)
                    pass
                else:
                    self.attr=attr
                    v=i[len(attr)+1:]
                    print("attribute found, save line to following attribute: ",attr,":", v)
                    
            else:
                print (self.attr,i)
            taskdata[attr]=v
            if i.strip()=="":
                l+=1
            if l==2:
                task=False
                self.attr=""
                print(taskdata)
#                     desc=taskdata["taskdescription"]
#                     desc="<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\"></style></head><body>"+desc+"</body></html>"
#                     taskdata["taskdescription"]=desc
#                     if self.checkIfExist(taskdata["taskname"]) is not True:
#                         duedate=time.mktime(time.strptime(taskdata["due"].strip(),dateformat))
#                         taskid = self.db.addTask(taskdata["taskname"],taskdata["priority"], taskdata["taskdescription"],duedate, self.currentContext)
#                         self.createTaskItem(taskdata["taskname"], taskid, int(taskdata["priority"]))
#                         self.adjustHeight()
#                         self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","Import finished."),3300)
#                     else:
#                         msg="cannot import task: "+taskdata["taskname"].strip()+", task with same name already exist on list.."
#                         msgWindow=QtGui.QMessageBox()
#                         msgWindow.information(self, "task already exist..", msg, buttons=QtGui.QMessageBox.Ok )
                        
                        
#             if entry==None and tag==0:
#                 task=False
#                 desc=taskdata["taskdescription"]
#                 desc="<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\"></style></head><body>"+desc+"</body></html>"
#                 taskdata["taskdescription"]=desc
#                 if self.checkIfExist(taskdata["taskname"]) is not True:
#                     duedate=time.mktime(time.strptime(taskdata["due"].strip(),dateformat))
#                     taskid = self.db.addTask(taskdata["taskname"],taskdata["priority"], taskdata["taskdescription"],duedate, self.currentContext)
#                     self.createTaskItem(taskdata["taskname"], taskid, int(taskdata["priority"]))
#                     self.adjustHeight()
#                     self.ui.statusbar.showMessage(QtGui.QApplication.translate("ui","Import finished."),3300)
#                 else:
#                     msg="cannot import task: "+taskdata["taskname"].strip()+", task with same name already exist on list.."
#                     msgWindow=QtGui.QMessageBox()
#                     msgWindow.information(self, "task already exist..", msg, buttons=QtGui.QMessageBox.Ok )
