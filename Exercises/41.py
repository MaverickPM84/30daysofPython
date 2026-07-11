'''
Exercise 41 - Letters in File

Question: Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.

'''
import string

list_text = string.ascii_lowercase

print(list(list_text))


# 'w' mode creates a new file or overwrites an existing one
with open("output.txt", "w") as file:
    for line in list_text:
        file.write(line + "\n")

'''
Solution 2 -

import string

with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")

The ascii_lowercase   property of the string  module is quite helpful here to generate a string of all letters. Then we create a file, and while the file is open, we iterate through the string and apply the write method in each iteration to write the letters in the text file. We are also appending \n  to each letter, which is a special character that creates break lines. That makes sure to separate the letters in different lines.


'''