'''
Beta
75. Exercise 34 - Local Vs. Global Variables
Open the course curriculum
Open the AI assistant
Open the course notes
Open the Q&A in a new tab
Exercise 34 - Local Vs. Global Variables

Question: The following script throws a NameError  in the last line saying that c  is not defined. Please fix the function so that there is no error and the  last line can print out the value of c  (i.e. 1 ).

def foo(): 
    c = 1 
    return c 
foo() 
print(c)
'''

#The reason for the error is that c  exists only inside the function namespace. In other words, c  is a local variable.
 
def foo(): 
    global c
    c = 1
    return c 
foo() 
print(c)

# Adding global c  fixes the code. That line makes available name c  in the global namespace. 
# Therefore,  print can access the variable c .