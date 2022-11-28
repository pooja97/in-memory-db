from collections import defaultdict
from array import Array
from object import Object
from transactions import Transactions

class DB:
    def __init__(self):
        self.database = defaultdict()
        self.transactions_data = []

    #adding data to the database.
    def put(self,key,value):
        if key not in self.database:
            if value is not None:
                self.database[key] = value
            else:
                return "Value cannot be Null"
        else:
            return "Key already exists in the database"


    #get Int value of the given key
    def getInt(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],int):
            return self.database[key]
        else:
            return "Not of type Int"

    #get String value of the given key
    def getString(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],str):
            return self.database[key]
        else:
            return "Not of type string"

    #get Double value of the given key
    def getDouble(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],float):
            return self.database[key]
        else:
            return "Not of type Double"
        
    #get Object value of the given key
    def getObject(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],object):
            return self.database[key]
        else:
            return "Not of type Object"

    #get array value of the given key
    def getArray(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],list):
            return self.database[key]
        else:
            return "Not of type Array"

    #get the value of the given key irrespective of type
    def get(self,key):
        if key not in self.database:
            return "Key does not exsist in the database"
        else:
            return self.database[key]

    #removing the given key from the database along with its value. 
    def remove(self,key):
        if key in self.database.keys():
            value = self.database.pop(key)
            return value
        else:
            return None

    def transaction(self):
        transaction = Transactions(self)
        return transaction


    #function for fetching and displaying the database
    def fetching_df(self):
        return self.database






