'''
Exercise 21 - Dictionary Filtering

Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

'''

d = {"a": 1, "b": 2, "c": 3}

filtered_d = {key: value for key, value in d.items() if value <= 1 }

print(filtered_d)