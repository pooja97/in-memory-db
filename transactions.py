class Transactions(object):
    transaction_stack = []

    def __init__(self,db_objs):
        self.db_objs = db_objs
    
    def put(self,command):
        putDB = command.execute()
        self.transaction_stack.append(command)
        return putDB

    def remove(self,command):
        removeDB = command.execute()
        self.transaction_stack.append(command)
        return removeDB

    def getInt(self,key):
        self.transaction_stack.append('getInt')
        return self.db_objs.getInt(key)

    def getString(self,key):
        self.transaction_stack.append('getString')
        return self.db_objs.getString(key)

    def getArray(self,key):
        self.transaction_stack.append('getArray')
        return self.db_objs.getArray(key)

    def getDouble(self,key):
        self.transaction_stack.append('getDouble')
        return self.db_objs.getDouble(key)

    def getObject(self,key):
        self.transaction_stack.append('getObject')
        return self.db_objs.getObject(key)

    def get(self,key):
        self.transaction_stack.append('get')
        return self.db_objs.get(key)

    #return False if transaction stack is empty and True if the transaction has been commited
    def commit(self):
        if not self.transaction_stack:
            return False
        else:
            return True

    def abort(self):
        if not self.transaction_stack:
            return 
        previous_transaction = self.transaction_stack.pop()
        if previous_transaction == ''


    # def isActive():
    #     pass 




