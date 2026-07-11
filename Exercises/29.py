'''

Beta
65. Exercise 29 - Liquid Volume Calculator
Open the course curriculum
Open the AI assistant
Open the course notes
Open the Q&A in a new tab
Exercise 29 - Liquid Volume Calculator

Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.


You can then test your solution by passing 2 for h and you should get the expected output.
'''
from math import pi

#default argument r = 10

def calc_volume(h, r = 10):
    volume = ((4 * pi * r**3)/3) - ((pi * h**2 * (3* r - h))/3)
    return(volume)

liquid_volume = calc_volume(2)
print(liquid_volume)
    