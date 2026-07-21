'''
Exercise 45 - One File per Letter

Question: Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b, and so on.

'''

import string

sample_str = string.ascii_lowercase
sample_list = list(sample_str)

for i in range(len(sample_list)):
    file_path = sample_list[i] + ".txt"
    with open(file_path, "w") as file:
        file.write(sample_list[i])


'''
Another solution with Files under a folder - 

import string, os

#create a folder which will include all the 26 files created

if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w) as file:
        file.write(letter + "\n")

'''