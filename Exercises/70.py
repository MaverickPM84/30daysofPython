

import requests

url = 'https://pythonhow.com/media/data/universe.txt'

response = requests.get(url, headers = {'user-agent': 'customUserAgent'})

text = response.text
letter_count = text.count('a')
# We're using the get method of the requests library here, which produces a response object. 
# Then we apply the text property to that response object to get the loaded web page's text.

print(text)
print(letter_count)

""" 
Here is a line-by-line breakdown of how your code works:

This approach uses the requests library, which is the most popular way to download data from the web in Python 

import requests This imports the external requests library. 


response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'}) 
This line does a few important things:

requests.get(...) sends an HTTP GET request to the URL to ask for the file.
headers = {'user-agent': 'customUserAgent'}: When you visit a website, 
your browser sends a "User-Agent" header to tell the website what kind of browser you are using (e.g., Chrome, Safari). 
Many websites block automated Python scripts to prevent bots from scraping their data. 
By adding this headers argument, you are faking your identity and telling the website 
that your name is "customUserAgent", which often bypasses these blocks.

The server's response is saved into the response variable.

text = response.text - Here, the .text property automatically looks at the data, 
figures out the text encoding, decodes the raw bytes behind the scenes, and gives you a perfectly clean Python string.

print(text) Finally, this prints the downloaded string to your terminal.

"""