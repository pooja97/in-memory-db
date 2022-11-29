'''
Author: Pooja Yadav
Created on: 11/29/2022
Red Id: 826102050

'''

from collections import defaultdict
from transactions import Transactions
from memento import Persistence
from cursor import Cursor

class DB:
    def __init__(self):
        self.database = defaultdict()
        self.transactions_data = []

    '''
    desc: Function for adding value in the database at the specified key
    input: Key and a value. Key is a string and value can be any list, array, double, object or string value
    output: returns database if data is added correctly else throws an exception

    '''
    def put(self,key,value):
        if key not in self.database:
            if value is not None:
                self.database[key] = value
            else:
                return "Value cannot be Null"
        else:
            return "Key already exists in the database"
        return self.database

    '''
    desc: Function for checking the type of the value at the specified key in the database
    input: String key
    output: returns the value of the key if it exists in the database and the type is int
    
    '''

    #get Int value of the given key
    def getInt(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],int):
            return self.database[key]
        else:
            return "Not of type Int"

    '''
    desc: Function for checking the type of the value at the specified key in the database
    input: String key
    output: returns the value of the key if it exists in the database and the type is string
    
    '''
    #get String value of the given key
    def getString(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],str):
            return self.database[key]
        else:
            return "Not of type string"

    '''
    desc: Function for checking the type of the value at the specified key in the database
    input: String key
    output: returns the value of the key if it exists in the database and the type is Double
    
    '''
    #get Double value of the given key
    def getDouble(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],float):
            return self.database[key]
        else:
            return "Not of type Double"
        

    '''
    desc: Function for checking the type of the value at the specified key in the database
    input: String key
    output: returns the value of the key if it exists in the database and the type is object
    
    '''
    #get Object value of the given key
    def getObject(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],object):
            return self.database[key]
        else:
            return "Not of type Object"

    '''
    desc: Function for checking the type of the value at the specified key in the database
    input: String key
    output: returns the value of the key if it exists in the database and the type is string

    '''
    #get array value of the given key
    def getArray(self,key):
        if key not in self.database.keys():
            return "Key does not exist in the database"
        elif isinstance(self.database[key],list):
            return self.database[key]
        else:
            return "Not of type Array"

    '''
    desc: Function for getting the value of the specified key in the database
    input: String key
    output: returns the value of the key if it exists in the database and the type is string

    '''
    #get the value of the given key irrespective of type
    def get(self,key):
        if key not in self.database:
            return "Key does not exsist in the database"
        else:
            return self.database[key]

    '''
    desc: Function for removing the value of the specified key from the database
    input: String key
    output: return None

    '''
    def remove(self,key):
        if key in self.database.keys():
            removed_key = key
            value = self.database.pop(key)
            return removed_key,value
        else:
            return None

    '''
    desc: Function for creating transaction object
    input: database object
    output: return Transaction class object

    '''
    def transaction(self):
        transaction = Transactions(self)
        return transaction

    '''
    desc: Function for creating snapshot with the default names
    input: database object
    output: returns empty Transaction stack after taking a snapshot 
    '''

    def snapshot(self):
        Persistence.save_memento_db(self.database)
        Transactions.transaction_stack = []

    '''
    desc: Function for creating snapshot with the specified file names
    input: database object
    output: returns empty Transaction stack after taking a snapshot 
    '''

    def snapshot_command(self,commands_file,database): 
        Persistence.save_memento(commands_file,database)
        Transactions.transaction_stack = []

    '''
    desc: Function for recovering database from the snapshot with the default parameters
    output: returns the database
    '''

    def recover(self):
        self.database = Persistence.get_memento() 
        
    '''
    desc: Function for recovering database from the snapshot with the specified parameters
    output: returns the database
    '''

    def recover_cmd(self,file_commands,file_snapshot):
        Persistence.get_memento_command(file_commands,file_snapshot)


    '''
    desc: Function for creating Cursor class object
    input: Key on which a cursor has to be created
    output: returns a Cursor object
    '''

    def getCursor(self,key):
        cursor_obj = Cursor(self.database[key])
        return cursor_obj







