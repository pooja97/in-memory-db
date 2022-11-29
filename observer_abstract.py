from abc import ABC, abstractmethod

class BaseObserver(ABC):
    '''
    Base observer class
    '''

    @abstractmethod
    def addObserver(self):
        pass 

    def removeObserver(self):
        pass