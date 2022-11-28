import json
class Persistence:
    pass
    # def __init__(self,data,filename ='file.tx',filesnapshot='untitled.txt'):
    #     self.data = data
    #     self.filename = filename
    #     self.filesnapshot = filesnapshot


    # def save_memento(self):
    #     with open(self.filename ,'w+') as file:
    #         file.write(json.dumps(self.data))
    #         file.close() 

    # def get_memento(self):
    #     try:
    #         with open(self.filename, 'r') as inventory_file:
    #             inventory_content = inventory_file.read()
    #             self.inventory_data = json.loads(inventory_content)

    #     except json.JSONDecodeError:
    #         print("Memento file is empty! Proceeding")