from base_command import BaseCommand
import json

class Remove(BaseCommand):
    def __init__(self,receiver,key):
        self.receiver = receiver
        self.key = key 

    def execute(self):
        '''
        desc: Executes the remove function of the receiver
        output: returns the removed value  
        '''
        value = self.receiver.remove(self.key)
        return value

    def put(self,value):
        '''
        desc: executes the put function of the receiver.
        input: value contains the key value pair
        '''
        return self.receiver.put(value)

    def toString(self):
        '''
        desc: Function for returning the string representation of the key
        '''
        return str(self.key)

