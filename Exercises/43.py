'''Exercise 43 - Letters Two by Two

Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.

'''
import string

list_text = string.ascii_lowercase

list_words = list(list_text)


# # # 'w' mode creates a new file or overwrites an existing one
with open("output1.txt", "w") as file:
    combined = ["".join(list_words[i:i+2]) for i in range(0, len(list_words), 2)]
    for item in combined:
        file.write(item + "\n")
    
