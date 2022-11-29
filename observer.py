class Observer:
    def __init__(self,Cursor):
        Cursor.addObserver(self)

    def notify(self,Cursor):
        return("Cursor object",Cursor)