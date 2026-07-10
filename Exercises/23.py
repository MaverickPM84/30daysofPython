
'''
Exercise 23 - Multilevel Indexing

Question: Access the third value of key b from the dictionary.

from pprint import pprint

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

'''

from pprint import pprint

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint(d)
pprint(d["b"][2])