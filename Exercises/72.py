# create a script that let the user type in a search term and opens and search the browser for that term of google
# Step 1: Take input from the user (the search term).
# Step 2: Construct the proper Google search URL using that term 
# (e.g., https://www.google.com/search?q=search_term).
# Step 3: Use a specific built-in Python module designed to open URLs in 
# the system's default web browser, and pass your constructed URL to it.

#https://www.google.com/search?q=python

import webbrowser
import urllib.parse

keyword = input("Enter the google search keywords: ")

# This converts spaces to '+' and safely encodes special characters
safe_keyword = urllib.parse.quote_plus(keyword)

url = f"https://www.google.com/search?q={safe_keyword}"

webbrowser.open_new_tab(url)

""" 
We're using webbrowser  here which is a standard library that is used to open a web browser.

First, we're getting the search term stored in variable query via the input function. 
You need to first do a manual search on Google and observe how Google will construct the URL.
Depending on where you are in the world the URL may be different, but the above URL should work everywhere.

You will see that the URL contains your search term at the end. 
Therefore, we concatenate the first part of the URL with the search term we get from input .

"""



