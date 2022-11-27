from array import Array
from object import Object
from db import DB 
from transactions import Transactions


if __name__ == 'main':
    #test cases
    db_obj = DB()
    db_obj.put('a',['b','c','d',123])
    db_obj.put('v',11.2000)
    db_obj.put('Bill',{'account 12343': {'name':'Bill', 'address':'123 main street', 'phones':['619-594-3535']}})
    db_obj.put('no',20121997)
    db_obj.put('name','Pooja')


    print("printing the database",db_obj.fetching_df())

    print("\n")
    print("\n")

    #testcases for getX method:
    print(db_obj.getInt('no'))
    print(db_obj.getObject('Bill'))
    print(db_obj.getDouble('v'))
    print(db_obj.getString('name'))
    print(db_obj.getArray('a'))


    #testcases for remove method:
    deleted_val_1 = db_obj.remove('Bill')
    print("Deleted value from the database is", deleted_val_1)

    deleted_val_2 = db_obj.remove('a')
    print("deleted value from the database is", deleted_val_2)

    print("Printing the database after removing the data from the database",db_obj.fetching_df())

    deleted_val_3 = db_obj.remove('z')
    print(deleted_val_3)

    #for storing array object
    arr = Array()
    arr.put("a")

    db_obj.put('string_val',arr)
    print("printing the database",db_obj.fetching_df())

    #for storing object
    object_class = Object()




