class Transactions(object):
    def __init__(self,db_objs):
        self.db_objs = db_objs
    
    def put(self,command):
        return command.execute()

    def remove(self,command):
        return command.execute()

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

    #return False if any transaction is not open and True if the transaction has been committed
    def commit(self):
        if not self.db_objs.transactions_data:
            return False
        self.db_objs.transactions_data += [{}]
        return True

    # def abort():
    #     pass 

    # def isActive():
    #     pass 




