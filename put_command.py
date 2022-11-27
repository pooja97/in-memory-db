from base_command import BaseCommand

class Put(BaseCommand):
    def __init__(self,receiver,key,data):
        self.receiver = receiver
        self.key = key 
        self.data = data 

    def execute(self):
        return self.receiver.put(self.key,self.data)