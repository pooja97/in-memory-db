import json
import shutil
class Persistence:
    def __init__(self,data):
        self.data = data
        
    def save_memento_db(data):
        with open('dbSnapshot.txt','w') as db_file:
            db_file.write(json.dumps(data))
            db_file.close()


    def save_memento(cmd_file,db_data):
        with open('commandSnapshot.txt','w') as cm_file:
            shutil.copy(cmd_file,'commandSnapshot.txt')
            cm_file.close()

        with open('dbSnapshot.txt','w') as db_file:
            db_file.write(json.dumps(db_data))
            db_file.close()


    #recover methods
    def get_memento(self):
        with open('./dbSnapshot.txt','r') as dbFile:
            content = dbFile
            dbFile.close()
            return content
    
    # def get_memento(self):
    #     pass

    