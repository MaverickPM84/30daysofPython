'''
Exercise 37 - Advanced Word Counter

Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.

'''


def word_counter(file_path):

    with open(file_path, 'r') as file:
        file_content = file.read()
    #A tree is a woody perennial plant,typically with branches.
    file_content = file_content.replace(",", " ")
    words_list = file_content.split()
    return(len(words_list))

file_path = "words2.txt"

num_of_words = word_counter(file_path)

print(num_of_words)

'''

ALternative method -

import re

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(",| ", text)
    return len(string_list)

print(count_words_re("words2.txt"))

This alternative solution uses the built-in re  module, which provides regular expression matching operations. We're using the split method of that module, and the expression ",| " is meant to replace commas with spaces. Using methods from the re  module can be more appropriate than Python built-in methods when string operations are complicated. However, for this simple scenario, the re  module could be skipped.


'''