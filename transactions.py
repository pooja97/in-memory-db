import json
class Transactions(object):
    transaction_stack = []

    def __init__(self,db_objs):
        self.db_objs = db_objs

    '''
    desc: Function for executing the specified command and appending the command to the transaction stack
    '''
    def put(self,command):
        putDB = command.execute()
        self.transaction_stack.append(command)
        return putDB

    '''
    desc: Function for executing remove command and adding the command to the transaction stack
    output: Returns the removed value
    '''
    def remove(self,command):
        self.removeDB = command.execute()
        self.transaction_stack.append(command)
        return self.removeDB

    '''
    desc: Function for checking the Int type of the value at the specified key in the database
    '''
    def getInt(self,key):
        return self.db_objs.getInt(key)

    '''
    desc: Function for checking the String type of the value at the specified key in the database
    '''

    def getString(self,key):
        return self.db_objs.getString(key)

    '''
    desc: Function for checking the Arraytype of the value at the specified key in the database
    '''
    def getArray(self,key):
        return self.db_objs.getArray(key)

    '''
    desc: Function for checking the Doubletype of the value at the specified key in the database
    '''
    def getDouble(self,key):
        return self.db_objs.getDouble(key)

    '''
    desc: Function for checking the Objecttype of the value at the specified key in the database
    '''
    def getObject(self,key):
        return self.db_objs.getObject(key)

    '''
    desc: Function for getting the value at the specified key from the database
    '''
    def get(self,key):
        return self.db_objs.get(key)


    '''return False if transaction stack is empty and True if the transaction has been commited'''
    def commit(self):
        if not self.transaction_stack:
            return False
        else:
            return True

    '''
    desc:Function for aborting the command and performing rollback
    '''
    def abort(self,command):
        if not self.transaction_stack:
            return 
        previous_transaction = self.transaction_stack.pop()
        if type(previous_transaction).__name__ == 'Put':
            command.remove(previous_transaction.key)
        else:
            command.put(previous_transaction.key,self.removeDB)
            self.transaction_stack.append(previous_transaction)

    '''
    desc: Function for writing the transaction stack to the file
    '''
    def writeCmdToFile(self,command_data):
        with open('commands.txt','w') as command_file:
            for x in command_data:
                command_file.write(str(type(x).__name__+'_'+x.toString()+'\n'))
            command_file.close()

    '''
    desc: function returns True if any transaction is active else False
    '''
    def isActive(self): 
        prev_len_transaction_stack = len(self.transaction_stack)
        if prev_len_transaction_stack == len(self.transaction_stack):
            return True 
        else:
            return False 




