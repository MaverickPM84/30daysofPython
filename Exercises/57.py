""" 
Exercise 57 - JSON to Dictionary

Question: Please download the file in the attachment and use Python to print out its content.

Expected output: 

{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
               {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}

Hint: This can be done through the json  and the pprint  built-in modules.

"""

import json, pprint

#open the file and parse its JSON content into a dict

with open('Exercises/company1.json', 'r') as file:
    data_dict = json.load(file)

print(type(data_dict))

pprint.pprint(data_dict)

""" 
Alternate solution with jons.loads

import json
from pprint import pprint

with open("company1.json","r") as file:
    d = json.loads(file.read())

pprint(d)

Explanation:

We're opening the file in read mode and then using json.loads  
which gets a string as output and creates a dictionary object out of that.


"""