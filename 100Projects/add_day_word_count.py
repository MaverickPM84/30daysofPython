"""
add day and number of words in the file to the filename
example filename = a.txt , the new filename should be - a-6-Thursday.txt


Steps:

1. Use python libraries 'os' to access the files, open them and datetime to extract day
2. use os lib to open the files directory to access the directory or folder in which the files are present
3. create a list of txt files in the files folder
4. loop over the files to first read them, count the number of words and then rename them

day = datetime.now().strftime("%A) - extract day , strftime is string from time

new_filepath = os.path.join(directory,new_filename)
os.rename(filepath, new_filepath)

"""

import os
from datetime import datetime

#step 1 - specify the directory where the files are located

directory = r"C:\Users\preet\OneDrive\Documents\30daysofPython\100Projects\files"


#step 2- get the list of files from the folder 


filenames = os.listdir(directory)


#step 2 - for each file, get the filename and rename it

for filename in filenames:
    #open and read the file to get the word count
    filepath = os.path.join(directory, filename)

    current_date = datetime.today().strftime('%Y-%m-%d')

    new_filename = f"{filename[:-4]}-{current_date}.txt"

    #create new filepath with new filename
    new_filepath = os.path.join(directory, new_filename)
    os.rename(filepath, new_filepath)

    print(f"Renamed {filename} with {new_filename}")

print("Renaming Complete")
    
