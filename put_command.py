from base_command import BaseCommand
class Put(BaseCommand):
    def __init__(self,receiver,key,data):
        self.receiver = receiver
        self.key = key 
        self.data = data 

    def execute(self):
        '''
        desc: executes the put function of the receiver
        output: returns the value returned from the put function of the receiver
        '''
        return self.receiver.put(self.key,self.data)

    def remove(self,key):
        '''
        desc: calls the remove function of the receiver
        output: returns the returned value of the remove function of the receiver
        '''
        return self.receiver.remove(key)

    def toString(self):
        '''
        desc: Function for returning the key value pair in a string format
        '''
        return str(self.key)+'-'+str(self.data)