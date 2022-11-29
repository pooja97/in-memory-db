import sys
class Object:
    def __init__(self):
        self.object_dict = {}

    def put(self,key,value):
        if key not in self.object_dict:
            if value is not None:
                self.object_dict[key] = value
            else:
                return "Values cannot be NULL"
        else:
            self.object_dict[key] = value
        return self.object_dict
    
    #check weather the value at the given key is an integer or not.
    def getInt(self,key):
        if key not in self.object_dict.keys():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],int):
            return self.object_dict[key]
        else:
            return "Not of type Int"

    #get String value of the given key
    def getString(self,key):
        if key not in self.object_dict.keys():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],str):
            return self.object_dict[key]
        else:
            return "Not of type string"

    #get Double value of the given key
    def getDouble(self,key):
        if key not in self.object_dict():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],float):
            return self.object_dict[key]
        else:
            return "Not of type Double"
        
    #get Object value of the given key
    def getObject(self,key):
        if key not in self.object_dict.keys():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],object):
            return self.object_dict[key]
        else:
            return "Not of type Object"

    #get array value of the given key
    def getArray(self,key):
        if key not in self.object_dict.keys():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],list):
            return self.object_dict[key]
        else:
            return "Not of type Array"

    #get the value of the given key irrespective of type
    def get(self,key):
        if key not in self.object_dict:
            return "Key does not exsist in the database"
        else:
            return self.object_dict[key]

    #removing the given key from the database along with its value. 
    def remove(self,key):
        if key in self.object_dict.keys():
            value = self.object_dict.pop(key)
            return value
        else:
            return None

    def toString(self):
        return str(self.object_dict)

    def fromString(self,string_value):
        return getattr(sys.modules[__name__], string_value)





