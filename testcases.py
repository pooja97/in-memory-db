from db import DB 
import unittest
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
    # print("After adding data: ",db_object.fetching_df())
    
    #commits the transactions
    invoker.commit()    
    print("transaction_stack after the commit: ", invoker.transaction_stack)
    print("database after the commit operation",db_object.fetching_df())

    
    #testcase for Null value input
    print(invoker.put(Put(db_object,'Last Name',None)))


    #testcase for remove command pattern
    invoker.remove(Remove(db_object,'d'))
    #testcase for checking the transaction stack after the remove operation
    invoker.commit()
 
    print("transaction_stack after the remove operation: ", invoker.transaction_stack)
    print("database after the remove operation and commit", db_object.fetching_df())

    #testcase for invalid key to remove
    print(invoker.remove(Remove(db_object,'First Name')))

    #testcase for get and getX method
    invoker.get('Number')
    invoker.getInt('Bill')
    invoker.getArray('name')
    invoker.getDouble('Number')


    #testcases for abort function : put command abort
    invoker.put(Put(db_object,'x',657))
    print("transaction stack after the put operation",invoker.transaction_stack)

    invoker.abort(db_object)
    print("transaction stack after the abort operation",invoker.transaction_stack)


 
    #testcases for abort function:remove command abort
    invoker.remove(Remove(db_object,'name'))
    invoker.abort(db_object)
    print("transaction stack after the abort operation",invoker.transaction_stack)



    print(invoker.write_cmd_to_file(invoker.transaction_stack))
    print("\n")
    print("\n")
    print("\n")

    print("final database",db_object.fetching_df())

    db_object.snapshot()
    db_object.snapshot_command('./commands.tx')











