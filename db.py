from collections import defaultdict
from transactions import Transactions
from memento import Persistence

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
        return self.database



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
            removed_key = key
            value = self.database.pop(key)
            return removed_key,value
        else:
            return None

    def transaction(self):
        transaction = Transactions(self)
        return transaction


    #change the parameter declaration
    def snapshot(self):
        Persistence.save_memento_db(self.database)
        

    #change the parameter declaration
    def snapshot_command(self,commands_file,database): 
        # database = self.database
        Persistence.save_memento(commands_file,database)

    
    def recover(self):
        Persistence.get_memento(self) 

    # def recover(self,file_commands,file_snapshot):
    #     pass

    


    #function for fetching and displaying the database
    def fetching_df(self):
        return self.database






