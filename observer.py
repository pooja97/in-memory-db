from observer_abstract import BaseObserver
class Observer(BaseObserver):
    def __init__(self):
        self.observers = []

    def addObserver(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)

        else:
            return "Failed to add observer"

    def removeObserver(self,observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

