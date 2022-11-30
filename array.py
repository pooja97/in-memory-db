import sys
'''
Array class
'''
class Array:
    def __init__(self):
        self.input_array = list()

    '''
    desc: Function for adding data to the array
    input: Value to be added to the array
    '''
    def put(self,value):
        self.input_array.append(value)

    '''
    desc: Function for getting the Int type of the specifed indexed value in the array
    input: array index
    output: value of the specified index from the array if it is of type int
    '''
    def getInt(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],int)== False:
            return "Not of type Int"
        else:
            return self.input_array[index]

    '''
    desc: Function for getting the string type of the specifed indexed value in the array
    input: array index
    output: value of the specified index from the array if it is of type string
    '''
    def getString(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],str)== False:
            return "Not of type String"
        else:
            return self.input_array[index]

    '''
    desc: Function for getting the double type of the specifed indexed value in the array
    input: array index
    output: value of the specified index from the array if it is of type double
    '''   
    def getDouble(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],float)== False:
            return "Not of type Double"
        else:
            return self.input_array[index]
    
    '''
    desc: Function for getting the double type of the specifed indexed value in the array
    input: array index
    output: value of the specified index from the array if it is of type Object
    ''' 
    def getObject(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],object)== False:
            return "Not of type Object"
        else:
            return self.input_array[index]


    '''
    desc: Function for getting the double type of the specifed indexed value in the array
    input: array index
    output: value of the specified index from the array if it is of type Array
    ''' 
    def getArray(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],list)== False:
            return "Not of type Array"
        else:
            return self.input_array[index]

    '''
    desc: Function for getting the value from the array at the specified index
    input: index value
    output: returns the value of the specified index from the array
    '''
    def get(self,index):
        if index > len(self.input_array):
            return "Index out of bound"
        else:
            return self.input_array[index]

    '''
    desc: Function for returning the length of the array
    output: returns the length of the array
    '''
    def length(self):
        return len(self.input_array)


    '''
    desc: Function for returning array as a string
    output: returns the string representation of an array
    '''
    def toString(self):
        return ''.join(self.input_array)


    '''
    desc: Function for removing the specified indexed value from the array
    input: index value
    output: returns the array
    '''
    def remove(self,index):
        return self.input_array.pop(index)
        

    '''
    desc: Function for returning the object from the string representation
    input: string value
    output: Object representation from the string value
    '''

    def fromString(self,string_value): 
        return getattr(sys.modules[__name__], string_value)