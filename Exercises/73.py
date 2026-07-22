#multiply the values of the text file in the URL by two and export the output to a new file

#Data in the file 
'''
x,y
3,5
4,9
6,10
7,11
8,12

'''
# Step 1 - http call to download the text file
# Step 2 - open the file in read/write mode
# Step 3 - for each of the numbers in the file, multiply by 2
# Step 4 - write the new numbers in a different file on my computer

# Hint: The easiest way to do this is with pandas.


import pandas as pd

url = 'https://pythonhow.com/data/sampledata.txt'

#create DataFrame by reading data using pandas

data = pd.read_csv(url)

#multiply the df by 2
updated_data = data * 2

#write to a file
updated_data.to_csv("updated.txt", index=False)


""" 
this can be done with pandas in four lines of code. 
We use read_csv to create a pandas dataframe object, which is like a table with data. 
Then we multiply this table by two and then export 
the calculated data to a text file in our local directory.

"""