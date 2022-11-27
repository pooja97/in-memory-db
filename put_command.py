from base_command import BaseCommand
# from db import DB

class Put(BaseCommand):
    def __init__(self,receiver,key,data):
        self.receiver = receiver
        self.key = key 
        self.data = data 

    def execute(self):
        self.receiver.put(self.key,self.data)