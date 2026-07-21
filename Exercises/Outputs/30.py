'''
Exercise 30 - Arguments

Question:  Why do you get an error, and how would you fix it?

def foo(a=2, b):
    return a + b

SyntaxError: parameter without a default follows parameter with a default
'''
#Always put non-default parameters first, followed by default ones.

def foo(b, a=2):
    return a + b


sum = foo(3)
print(sum)