class Transactions(object):
    def put(self,command):
        command.execute()

    # def getX(self, key):
    #     pass 

    # def get(self, key):
    #     pass

    def remove(self,command):
        command.execute()


    # def commit():
    #     pass

    # def abort():
    #     pass 

    # def isActive():
    #     pass 



#transaction class will be invoker and db class will be receiver
#invoker class will have register and execute method

