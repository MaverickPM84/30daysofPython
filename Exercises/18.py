'''
Find the error in this code and correct it -

Code- 
d = {"Name": "John", "Surname": "Smith"}
print(d["Smith"])
'''
# In the code,we get A KeyError always means Python could not find a key with the name shown next to KeyError (e.g. Smith ).

#correct way - There is no key Smith  in the dictionary. Smith  is a value. You want to use Surname  if you want to access Smith :

d = {"Name": "John", "Surname": "Smith"}
print(d["Surname"])