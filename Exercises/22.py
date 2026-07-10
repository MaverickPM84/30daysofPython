'''
Exercise for reference: 

Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30, respectively. 
Then print out the dictionary in a nice format.

'''

from pprint import pprint

range_1 = range(1,11)

list_1 = list(range_1)



range_2 = range(11,21)

list_2 = list(range_2)



range_3 = range(21,31)

list_3 = list(range_3)

d = {}

d["a"] = list_1

d["b"] = list_2

d["c"] = list_3

#The built-in pprint module splits nested structures and long dictionaries across multiple lines automatically.

pprint(d, indent=1)

#Faster Way

dict = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(dict)