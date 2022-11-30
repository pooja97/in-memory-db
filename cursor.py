#Observable class
class Cursor:
    def __init__(self,cursor):
        self.cursor = cursor
        self.observers = []

    '''
    desc: Function for checking the type of the value at the specified key in the cursor
    input: String key
    output: returns the value of the key if its type is int
    '''
    def getInt(self):
        if isinstance(self.cursor,int):
            return "Instance of an Int"
        else:
            return "Invalid type"
    
    '''
    desc: Function for checking the type of the value at the specified key in the cursor
    input: String key
    output: returns the value of the key if it is of type is string
    
    '''
    def getString(self):
        if isinstance(self.cursor,str):
            return "Instance of a string"
        else:
            return "Invalid type"

    '''
    desc: Function for checking the type of the value at the specified key in the cursor
    input: String key
    output: returns the value of the key if it is of type Double
    
    '''
    def getDouble(self):
        if isinstance(self.cursor,float):
            return "Instance of a double"
        else:
            return "Invalid type"

    '''
    desc: Function for checking the type of the value at the specified key in the cursor
    input: String key
    output: returns the value of the key if it is of type object
    '''
    def getObject(self):
        if isinstance(self.cursor,object):
            return "Instance of an object"
        else:
            return "Invalid type"
        
    '''
    desc: Function for getting the value of the specified key 
    input: String key
    output: returns the value of the key if it of type string
    '''
    def get(self):
        return self.cursor


    '''
    DESC: Function for adding the observer
    '''
    def addObserver(self, observer):
        self.observers.append(observer)

    '''
    Function for removing the observer
    '''
    def removeObserver(self,observer):
        self.observers.remove(observer)

    '''
    Function for notfying the state Change
    '''
    def notify_observers(self,*args,**kwargs):
        for obs in self.observers:
            obs.notify(self)


