class Transactions(object):
    transaction_stack = []

    def __init__(self,db_objs):
        self.db_objs = db_objs

    
    def put(self,command):
        putDB = command.execute()
        self.transaction_stack.append(command)
        return putDB

    def remove(self,command):
        self.removeDB = command.execute()
        self.transaction_stack.append(command)
        return self.removeDB

    def getInt(self,key):
        return self.db_objs.getInt(key)

    def getString(self,key):
        return self.db_objs.getString(key)

    def getArray(self,key):
        return self.db_objs.getArray(key)

    def getDouble(self,key):
        return self.db_objs.getDouble(key)

    def getObject(self,key):
        return self.db_objs.getObject(key)

    def get(self,key):
        return self.db_objs.get(key)

    #return False if transaction stack is empty and True if the transaction has been commited
    def commit(self):
        if not self.transaction_stack:
            return False
        else:
            return True

    def abort(self,command):
        if not self.transaction_stack:
            return 
        previous_transaction = self.transaction_stack.pop()
        if type(previous_transaction).__name__ == 'Put':
            command.remove(previous_transaction.key)
        else:
            command.put(previous_transaction.key,self.removeDB)
            self.transaction_stack.append(previous_transaction)

    def write_cmd_to_file(self,command_data):
        with open('commands.txt','w') as command_file:
            for x in command_data:
                command_file.write(str(type(x).__name__+' : '+x.toString()+'\n'))
            command_file.close()

    def isActive(self): #need help
        prev_len_transaction_stack = len(self.transaction_stack)
        if prev_len_transaction_stack == len(self.transaction_stack):
            return True 
        else:
            return False 




