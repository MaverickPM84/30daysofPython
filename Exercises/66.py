""" 
Exercise 66 - Translator

Question: Create an English to Portuguese translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

Expected output: 

Enter word: earth
terra

Hint: It's good to create a function that takes the user input and uses it as a key to access the corresponding dictionary value.


Step 1 - take input from user pass it to a function that translates the word based on the dictionary
Step 2 - create a function that takes in the word given by the user and return the translation
Step 3 - print the translation

"""

d = dict(weather = "clima", earth = "terra", rain = "chuva") 


def translate(word):
    return d[word]


user_input = input("Enter the word:  ")
translated_word = translate(user_input)
print(f"Translation of {user_input} is {translated_word}")
