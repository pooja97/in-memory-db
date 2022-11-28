from db import DB 
from put_command import Put
from remove_command import Remove


if __name__ == '__main__':
    
    db_object = DB() 

    invoker = db_object.transaction()
    invoker1 = db_object.transaction()

    #testcase for put command pattern 
    invoker.put(Put(db_object,'name','Pooja'))
    invoker.put(Put(db_object,'Bill',{'account 12343': {'name':'Bill', 'address':'123 main street', 'phones':['619-594-3535']}}))
    invoker.put(Put(db_object,'Number',1234567989))
    invoker.put(Put(db_object,'Dob',12201997))
    invoker.put(Put(db_object,'d',123))

    #For checking the database after adding data
    print("After adding data: ",db_object.fetching_df())
    
    #commits the transactions
    invoker.commit()    
    print("transaction_stack after the commit: ", invoker.transaction_stack)

    
    #testcase for Null value input
    print(invoker.put(Put(db_object,'Last Name',None)))


    #testcase for remove command pattern
    invoker.remove(Remove(db_object,'d'))
    print("Database after removing the given key: ",db_object.fetching_df())

    #testcase for checking the transaction stack after the remove operation
    invoker.commit()    
    print("transaction_stack after the remove operation: ", invoker.transaction_stack)

    #testcase for invalid key to remove
    print(invoker.remove(Remove(db_object,'First Name')))

    #testcase for get and getX method
    invoker.get('Number')
    invoker.getInt('Bill')
    invoker.getArray('name')
    invoker.getDouble('Number')

    invoker.commit()
    print("transaction stack after the get and getX methods", invoker.transaction_stack)

    invoker.abort()

    print("transaction stack after the abort command", invoker.transaction_stack)








