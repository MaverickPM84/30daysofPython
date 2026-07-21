'''
Exercise 26 - Print Range

Question: Make a script that prints out numbers from 1 to 10

'''
#print on separate lines
for i in range(1,11):
    print(i)

#print on same line
for i in range(1,11):
    print(i, end="")      #by default print adds a \n newline at the end so in the first method numbers are printed on newline.


# A for  loop is used to repeat an action (i.e. print ) until the iterating sequence (i.e. range ) is consumed. 
# In our case, it would print all items of the range one by one.