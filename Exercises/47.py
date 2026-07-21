# write a script that iterates thru each of the files, checks if the letter inside the text file is in string "python"
# if the letter is a character in "python" put it in a list

# Step 1 - access the folder that contains all the files usng glob library
# Step 2a - iterate over the folder to read the files one by one.
# Step 2b - Step 2b — after reading, clean/strip the content before comparing
# Step 3 -  check if character in the file equals character in "python" and if it is True put it in the list
# Step 4 -  print the list


import glob

compare_string = "python"
letters = []

file_list = glob.glob("Exercises/*.txt")

for filename in file_list:
    with open(filename, "r") as file:
        char = file.read().strip("\n")
    if char in compare_string:
        letters.append(char)


print(letters)