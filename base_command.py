from abc import ABC, abstractmethod

'''
Abstract class for command pattern
'''

class BaseCommand(ABC):
    '''
    Base command class
    '''

    @abstractmethod
    def execute(self):
        pass 