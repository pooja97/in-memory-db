from base_command import BaseCommand

class Remove(BaseCommand):
    def __init__(self,receiver,key):
        self.receiver = receiver
        self.key = key 

    def execute(self):
        return self.receiver.remove(self.key)