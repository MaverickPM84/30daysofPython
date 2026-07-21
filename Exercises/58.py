'''
Exercise 58 - Add to JSON

Question: Please download the json file in the attachment and 
use Python to add a new employee to the file's content so that 
the file looks like in the expected output below.

Breakdown -
Step 1 - Read the json file
Step 2 - Create a dictionary using the content in the file
Step 3 - Add a new employee - key value pair in the dict
Step 4 - seek file.seek(0) to put the cursor at the top of the file
Step 5 - convert the dict to json , dump the dict to the opened file again

'''

import json

with open('Exercises/company1.json', 'r+') as file:
    
    data_dict = json.loads(file.read())
    
    data_dict['employees'].append(dict(firstName = "Preetam", lastName = "Kale"))

    file.seek(0)

    json.dump(data_dict, file, indent = 4, sort_keys=True)

    file.truncate()



