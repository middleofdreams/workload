import os,datetime
def export(tasks,filename,dateformat):
    out="taskname,taskdescription,created,priority,due,closed,closedat"
    for i in tasks:
        ln=""
        for attr in i:
            index=i.index(attr)
            if attr is None:
                attr=""
            if isinstance(attr,int):
                attr=str(attr)
            if index==2 or index==4 or index==6:
                d=datetime.datetime.fromtimestamp(float(attr))
                attr=d.strftime(dateformat)
            attr=attr.replace(",","%comma%")
            attr=attr.replace("\n","%newline%")
            attr=attr.replace("\r\n","%newline")
            ln+=attr+","
        out+=os.linesep.encode('utf-8')+ln[:-1]
    f=open(filename,'wb')
    f.write(out)
    f.close()