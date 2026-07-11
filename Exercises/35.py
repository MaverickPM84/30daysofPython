'''
Exercise 35 - String Splitter

Question: Create a function that takes any string as input and returns the number of words for that string.
'''


def word_count(name):
    word_list = name.split()
    return(len(word_list))

name = "My name is Preetam"

num_of_words = word_count(name)

print(num_of_words)

# We're using split  here which is a string method that splits a string into several strings given a separator passed inside the brackets. 
# When you don't pass a separator, split  will split a string at white spaces. This will output a list of strings.
# Applying len  to that list returns the number of list items, so the number of words.