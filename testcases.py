from db import DB 
from put_command import Put
from remove_command import Remove


if __name__ == '__main__':
    
    db_object = DB() 

    #opens transaction block
    db_object.transactions_data+=[{}]

    invoker = db_object.transaction()
    invoker1 = db_object.transaction()

    #testcase for put command pattern 
    invoker.put(Put(db_object,'name','Pooja'))
    invoker.put(Put(db_object,'Bill',{'account 12343': {'name':'Bill', 'address':'123 main street', 'phones':['619-594-3535']}}))
    invoker.put(Put(db_object,'Number',1234567989))
    invoker.put(Put(db_object,'Dob',12201997))
    invoker.put(Put(db_object,'d',123))
    
    #commits the transactions
    invoker.commit()


    print("After adding data: ",db_object.fetching_df())


    #testcase for Null value input
    print(invoker.put(Put(db_object,'Last Name',None)))

    invoker1.put(Put(db_object,'e',134))

    #testcase for remove command pattern
    invoker.remove(Remove(db_object,'d'))
    print("Database after removing the given key: ",db_object.fetching_df())

    #testcase for invalid key to remove
    print(invoker.remove(Remove(db_object,'First Name')))

    #testcase for get and getX method
    print(invoker.get('Number'))
    print(invoker.getInt('Bill'))
    print(invoker.getArray('name'))
    print(invoker.getDouble('Number'))
    print(invoker.commit())










   
    # print(db_obj.getInt('no'))
    # print(db_obj.getObject('Bill'))
    # print(db_obj.getDouble('v'))
    # print(db_obj.getString('name'))
    # print(db_obj.getArray('a'))


    # #testcases for remove method:
    # deleted_val_1 = db_obj.remove('Bill')
    # print("Deleted value from the database is", deleted_val_1)

    # deleted_val_2 = db_obj.remove('a')
    # print("deleted value from the database is", deleted_val_2)

    # print("Printing the database after removing the data from the database",db_obj.fetching_df())

    # deleted_val_3 = db_obj.remove('z')
    # print(deleted_val_3)

    # #for storing array object
    # arr = Array()
    # arr.put("a")

    # db_obj.put('string_val',arr)
    # print("printing the database",db_obj.fetching_df())

    # #for storing object
    # object_class = Object()




