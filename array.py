class Array:
    def __init__(self):
        self.input_array = list()

    def put(self,value):
        self.input_array.append(value)

    def getInt(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],int)== False:
            return "Not of type Int"
        else:
            return self.input_array[index]


    def getString(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],str)== False:
            return "Not of type String"
        else:
            return self.input_array[index]
          

    def getDouble(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],float)== False:
            return "Not of type Double"
        else:
            return self.input_array[index]
    

    def getObject(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],object)== False:
            return "Not of type Object"
        else:
            return self.input_array[index]

    def getArray(self,index):
        if index>len(self.input_array):
            return "Index out of bound"
        elif isinstance(self.input_array[index],list)== False:
            return "Not of type Array"
        else:
            return self.input_array[index]


    def get(self,index):
        if index > len(self.input_array):
            return "Index out of bound"
        else:
            return self.input_array[index]

    def length(self):
        return len(self.input_array)

    def toString(self):
        return ''.join(self.input_array)

    def remove(self,index):
        return self.input_array.pop(index)
        

    def fromString(self,string_value): #not able to understand need help with this
        pass