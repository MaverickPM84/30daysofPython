

import requests

headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])


"""

Hint 1: The code generates an error that suggests the requests module does not have a get  method. 
The requests library does actually have a get  method.


Hint 2: Import statements first look for a local file in the current directory (e.g., requests.py). 
If there is such a file, it imports that file and not the actual module. 

Read the error carefully - 

AttributeError: module 'requests' has no attribute 'get' 
-> (consider renaming 'c:\Users\preet\OneDrive\Documents\30daysofPython\Exercises\Outputs\requests.py' if it has the same name as a library you intended to import)

"""