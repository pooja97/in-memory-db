import json
class Persistence:
    def __init__(self,data):
        self.data = data
        
    def save_memento(data):
        with open('dbSnapshot.txt','w') as db_file:
            db_file.write(json.dumps(data))
            db_file.close()


    

    # def get_memento(self):
    #     try:
    #         with open(self.filename, 'r') as inventory_file:
    #             inventory_content = inventory_file.read()
    #             self.inventory_data = json.loads(inventory_content)

    #     except json.JSONDecodeError:
    #         print("Memento file is empty! Proceeding")