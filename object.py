import sys
class Object:
    def __init__(self):
        self.object_dict = {}

    '''
    desc: Function for adding data to the object dictionary
    input: Value to be added to the object dictionary
    output: returns the object dictionary
    '''
    def put(self,key,value):
        if key not in self.object_dict:
            if value is not None:
                self.object_dict[key] = value
            else:
                return "Values cannot be NULL"
        else:
            self.object_dict[key] = value
        return self.object_dict

    '''
    desc: Function for getting the Int type of the specifed key in the object dictionary
    input: key
    output: value of the specified key from the object dictionary if it is of type int
    '''
    def getInt(self,key):
        if key not in self.object_dict.keys():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],int):
            return self.object_dict[key]
        else:
            return "Not of type Int"

    '''
    desc: Function for getting the String type of the specifed key in the object dictionary
    input: key
    output: value of the specified key from the object dictionary if it is of type String
    '''
    def getString(self,key):
        if key not in self.object_dict.keys():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],str):
            return self.object_dict[key]
        else:
            return "Not of type string"

    '''
    desc: Function for getting the double type of the specifed key in the object dictionary
    input: key
    output: value of the specified key from the object dictionary if it is of type double
    '''
    def getDouble(self,key):
        if key not in self.object_dict():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],float):
            return self.object_dict[key]
        else:
            return "Not of type Double"

    
    '''
    desc: Function for getting the object type of the specifed key in the object dictionary
    input: key
    output: value of the specified key from the object dictionary if it is of type object
    '''    
    def getObject(self,key):
        if key not in self.object_dict.keys():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],object):
            return self.object_dict[key]
        else:
            return "Not of type Object"


    '''
    desc: Function for getting the array type of the specifed key in the object dictionary
    input: key
    output: value of the specified key from the object dictionary if it is of type array
    '''

    def getArray(self,key):
        if key not in self.object_dict.keys():
            return "Key does not exist in the database"
        elif isinstance(self.object_dict[key],list):
            return self.object_dict[key]
        else:
            return "Not of type Array"

    '''
    desc: Function for getting the value from the object dictionary
    input: key
    output: returns the value from object dictionary of the specified key
    '''
    def get(self,key):
        if key not in self.object_dict:
            return "Key does not exsist in the database"
        else:
            return self.object_dict[key]


    '''
    desc: Function for removing the value from the object dictionary
    input: key
    output: returns the value from object dictionary of the specified key after removing the value
    '''
    def remove(self,key):
        if key in self.object_dict.keys():
            value = self.object_dict.pop(key)
            return value
        else:
            return None

    '''
    desc: Function for converting the object to a string representation
    output: returns the string representation of the object dictionary
    '''
    def toString(self):
        return str(self.object_dict)

    '''
    desc: Function for converting to an object representation from the string
    output: returns the object representation from the string
    '''
    def fromString(self,string_value):
        return getattr(sys.modules[__name__], string_value)





