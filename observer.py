class Observer:
    def __init__(self,Cursor):
        Cursor.addObserver(self)

    '''
    desc: notify function for notifying the cursor
    '''
    def notify(self,Cursor):
        return("Cursor object",Cursor)