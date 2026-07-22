
# Password checker - length - 5 digits, atleast 1 uppercase letter, atleast 1 number

while True:
    user_password = input("Enter your password: ")

    # Check length, check for at least one number, check for at least one uppercase
    if len(user_password) >= 5 and any(char.isdigit() for char in user_password) and any(char.isupper() for char in user_password):
        print("Password is fine")
        break
    else:
        print("Password is not fine. Please try again.")


"""
We're using a while loop here because we need to keep the program running until 
the user submits a password that satisfies all three conditions. 
Line 8 contains the three conditions connected with an and  operator. 
Line 8 becomes True  only when all three conditions are True . 
If that happens, Password is fine  is generated, and the break statement will break the loop, 
and the program will stop. 
If at least one of the conditions in Line 8 is False Line 8 evaluates to False  
and the print  statement under else is executed, 
and the loop starts over again.

""" 