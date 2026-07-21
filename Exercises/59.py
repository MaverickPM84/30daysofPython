""" 
Exercise 59 - Enumerator

Question: Please complete the code so that it prints out the expected output.

a = [1, 2, 3] 

Expected output: 

Item 1 has index 0
Item 2 has index 1
Item 3 has index 2

Hint 1: Use a for  loop.


Hint 2: Iterate through enumerate(a) .

"""

a = [1, 2, 3]

for index, item in enumerate(a):
    print(f"Item {item} has index {index}")