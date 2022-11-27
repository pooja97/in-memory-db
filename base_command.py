from abc import ABC, abstractmethod

class BaseCommand(ABC):
    '''
    Base command class
    '''

    @abstractmethod
    def execute(self):
        pass 