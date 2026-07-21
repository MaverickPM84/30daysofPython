# write a script to extract letters from the 26 text files and put the letters in a list

# step 1 - identify the folder in which the 26 files lie

import os
from pathlib import Path

#access the folder, i need to know the path/dir and then need to get the list of files from the dir

dir_path = Path('Exercises')
files_list = list(dir_path.glob('*.txt'))

all_content = []

for file in files_list:
    with open(file, 'r') as file:
        all_content.append(file.read().strip("\n"))

print(all_content)
# step 2 - read the files one by one and extract the letter

# step 3 - create a list and add the letter to the list


'''

Another solution

import glob

letters = []

file_list = glob,glob("Exercises/*.txt")

for filename in file_list:
    with open(filename, "r) as file:
        letters.append(file.read().strip("\n"))

print(letters)

'''