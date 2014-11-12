import datetime

def timestamp(dateobject):
        '''for python 2 compatibility'''
        try:
            timestamp = dateobject.timestamp()
        except AttributeError:
            timestamp = (dateobject - datetime.datetime(1970, 1, 1)).total_seconds()
            
        return timestamp
    
def QtDateFormat(df):
    df=df.replace("%H","HH")
    df=df.replace("%d","dd")
    df=df.replace("%Y","yyyy")
    df=df.replace("%y","yy")
    df=df.replace("%M","mm")
    df=df.replace("%m","MM")
    return df