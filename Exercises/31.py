'''
Exercise 31 - Function Blueprint

Question:  Why is there an error in the code, and how would you fix it?

def foo(a=1, b=2):
    return a + b

x = foo - 1

() missing

error - Type Error - using wrong object type to do the operation

foo without the () is of type - function - check print(type(foo)), but if you use foo() it is of type int

'''

def foo(a = 1, b=2):
    return(a + b)

x = foo() - 1