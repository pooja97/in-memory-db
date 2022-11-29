from base_command import BaseCommand
import json

class Remove(BaseCommand):
    def __init__(self,receiver,key):
        self.receiver = receiver
        self.key = key 

    def execute(self):
        value = self.receiver.remove(self.key)
        return value

    def put(self,value):
        return self.receiver.put(value)

    def toString(self):
        return str(self.key)

