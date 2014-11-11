import datetime

def timestamp(dateobject):
        '''for python 2 compatibility'''
        try:
            timestamp = dateobject.timestamp()
        except AttributeError:
            timestamp = (dateobject - datetime.datetime(1970, 1, 1)).total_seconds()
            
        return timestamp