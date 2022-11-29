#publisher class
from observer import Observer
class Cursor:
    def __init__(self,cursor):
        self.cursor = cursor

    def getX(self):
        if isinstance(self.cursor,int):
            return "Instance of an Int"
        elif isinstance(self.cursor,str):
            return "Instance of a string"
        elif isinstance(self.cursor,float):
            return "Instance of a double"
        elif isinstance(self.cursor,object):
            return "Instance of an object"
        else:
            return "Invalid type"
        
    def get(self):
        return self.cursor

    def addObserver(self,):
        Observer.addObserver(self, self.cursor)

    def removeObserver(self):
        Observer.removeObserver(self,self.cursor)

