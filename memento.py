import json
import shutil
class Persistence:
    def __init__(self,data):
        self.data = data
        
    def saveMementodb(data):
        with open('dbSnapshot.txt','w') as db_file:
            db_file.write(json.dumps(data))
            db_file.close()

    def saveMemento(cmd_file,db_data):
        with open('commandSnapshot.txt','w') as cm_file:
            shutil.copy(cmd_file,'commandSnapshot.txt')
            cm_file.close()
        with open('dbSnapshot.txt','w') as db_file:
            db_file.write(json.dumps(db_data))
            db_file.close()


    #recover methods
    def getMemento():
        with open('./dbSnapshot.txt','r') as dbFile:
            content = json.load(dbFile)
            dbFile.close()
        with open('./commands.txt','r') as cmds_file:
            for i in cmds_file:
                cmd = i.split('_')[0]
                val = i.split('_')[1]
                if cmd == 'Put':
                    #do something with put
                    val = str(val).strip()
                    val_list = val.split("-")
                    key = val_list[0]
                    value = val_list[1]
                    content[key]=value

                elif cmd == 'Remove':
                    #do something with val
                    if key not in content:
                        return "Invalid key"
                    else:
                        del content[key]
            cmds_file.close() 
        return content
    
    def getMementoCommand(cmd_file,db_snapshot):
        with open(db_snapshot,'r') as dbFile:
            content = json.load(dbFile)
            dbFile.close()

        with open(cmd_file,'r') as cmds_file:
            for i in cmds_file:
                cmd = i.split('_')[0]
                val = i.split('_')[1]
                if cmd == 'Put':
                    #do something with put
                    val = str(val).strip()
                    val_list = val.split("-")
                    key = val_list[0]
                    value = val_list[1]
                    content[key]=value

                elif cmd == 'Remove':
                    #do something with val
                    if key not in content:
                        return "Invalid key"
                    else:
                        del content[key] 
            cmds_file.close()    
        return content

    