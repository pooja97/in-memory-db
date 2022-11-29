import json
class Persistence:
    def __init__(self,data):
        self.data = data
        
    def save_memento(data):
        with open('dbSnapshot.txt','w') as db_file:
            db_file.write(json.dumps(data))
            db_file.close()


    def save_memento(self,cmd_file,db_data):
        with open('commandSnapshot.txt','w') as cm_file:
            cm_file.write(json.dumps(cmd_file))
            cm_file.close()

        with open('dbSnapshot.txt','w') as db_file:
            db_file.write(json.dumps(db_data))
            db_file.close()

    