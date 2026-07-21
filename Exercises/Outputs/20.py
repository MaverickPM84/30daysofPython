'''
Exercise 20 - Apply Function to Dictionary Items

Question: Calculate the sum of all dictionary values.
d = {"a": 1, "b": 2, "c": 3}

'''

d = {"a": 1, "b": 2, "c": 3}

total_sum = sum(d.values())

print(total_sum)

#The fastest and most Pythonic way to sum all values in a dictionary is to 
#combine Python's built-in sum() function with the dictionary's .values() method.

#d.values() returns a list-like dict_values object
#while the sum  function calculates the sum of the dict_values items.