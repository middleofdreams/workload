import os,datetime,codecs
def export(tasks,filename,dateformat):
    out="taskname,taskdescription,created,priority,due,closed,closedat"
    for i in tasks:
        ln=""
        for attr in i:
            index=i.index(attr)
            if attr is None:
                attr=""
            if isinstance(attr,int):
                attr=bytes(attr).decode()
            if index==2 or index==4 or index==6:
                attr=attr.split(".")[0].strip()
                try:
                    attr=int(attr)
                except:
                    continue
                d=datetime.datetime.fromtimestamp(int(attr))
                attr=d.strftime(dateformat)
            attr=attr.replace(",","%comma%")
            attr=attr.replace("\n","%newline%")
            attr=attr.replace("\r\n","%newline")
            ln+=attr+","
        out+="\r\n"+ln[:-1]
    f=codecs.open(filename,'w','utf-8')
    f.write(out)
    f.close()