# # Area Calculator
# Create a calculator.py program that calculates the area of one of the following shapes:

# Square
# Rectangle
# Triangle
# Circle
# The program should present a menu for the user to choose which shape to calculate, then ask them for the appropriate values (side, length, width, etc.).

# Then, it should calculate the area and print it out.

# pi = 3.14

# The output should look something like this:

# ==================
# Area Calculator 📐
# ==================

# 1) Triangle
# 2) Rectangle
# 3) Square
# 4) Circle
# 5) Quit

# Which shape: 1

# Base: 5
# Height: 6

# The area is 15


print("-----------------\n")
print("Area Calculator \n")
print("-----------------\n")

print("Which shape area do you want to calculate ? \n")
print("Enter: \n")
print("1 for Triangle \n")
print("2 for Rectangle \n")
print("3 for Square \n")
print("4 for Circle \n")
print("5 to Quit \n")

shape = int(input("Which shape:  "))

#area of a triangle

if shape == 1:
    height = float(input("Enter the height in cms: "))
    base = float(input("Enter the base in cms: "))
    area = (height * base) / 2
    print(f"The area is {area}")
    

#area of a rectangle

elif shape == 2:

    length = float(input("Enter the length in cms: "))
    width = float(input("Enter the width in cms: "))
    area = length * width
    print(f"The area is {area}")

#area of a square

elif shape == 3:

    side = float(input("Enter the side in cms: "))
    area = side ** 2
    print(f"The area is {area}")

#area of a circle

elif shape == 4:

    radius = float(input("Enter the radius in cms: "))
    area = radius * (3.14 ** 2)
    print(f"The area is {area}")

else:

    print("You have exited the program !!")