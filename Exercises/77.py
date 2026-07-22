""" 
Exercise 77 - Year of Birth Calculator

Question: Create a script that asks the user to enter their age, 
and the script calculates the user's year of birth and 
prints it out in a string like in the expected output. 
Please make sure you generate the current year dynamically.

Expected output: 

We think you were born back in 1988

1. Get age
2. Take current year
3. current year - age

"""

from datetime import datetime

age = int(input("Enter your age: "))

current_year = int(datetime.now().strftime("%Y"))

birth_year = current_year - age

print(f"We think you were born back in {birth_year}")

