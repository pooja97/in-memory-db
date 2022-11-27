class Transactions(object):
    def put(self,command):
        return command.execute()

    def remove(self,command):
        return command.execute()

    def getInt(self, DB, key):
        return DB.getInt(key)

    def getString(self,DB,key):
        return DB.getString(key)

    def getArray(self,DB,key):
        return DB.getArray(key)

    def getDouble(self,DB,key):
        return DB.getDouble(key)

    def getObject(self,DB,key):
        return DB.getObject(key)


    def get(self,DB,key):
        return DB.get(key)
        

    # def commit():
    #     pass

    # def abort():
    #     pass 

    # def isActive():
    #     pass 




