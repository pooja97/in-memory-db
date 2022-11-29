#Observable class
class Cursor:
    def __init__(self,cursor):
        self.cursor = cursor
        self.observers = []

    def getInt(self):
        if isinstance(self.cursor,int):
            return "Instance of an Int"
        else:
            return "Invalid type"
            
    def getString(self):
        if isinstance(self.cursor,str):
            return "Instance of a string"
        else:
            return "Invalid type"

    def getDouble(self):
        if isinstance(self.cursor,float):
            return "Instance of a double"
        else:
            return "Invalid type"

    def getObject(self):
        if isinstance(self.cursor,object):
            return "Instance of an object"
        else:
            return "Invalid type"
        
    def get(self):
        return self.cursor

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self,observer):
        self.observers.remove(observer)

    def notify_observers(self,*args,**kwargs):
        for obs in self.observers:
            obs.notify(self)


