

while True:

    user_password = input("Enter your password: ")

    # Check length, check for at least one number, check for at least one uppercase
    if len(user_password) < 5 and not any(char.isdigit() for char in user_password) and not any(char.isupper() for char in user_password):
        print("Password length should be greater than or equal to 5 characters")
        print("There should be at least 1 number in the password")
        print("Password should contain at least 1 capital letter")

    elif len(user_password) >= 5 and not any(char.isdigit() for char in user_password) and not any(char.isupper() for char in user_password):
        print("There should be at least 1 number in the password")
        print("Password should contain at least 1 capital letter")

    elif len(user_password) >= 5 and any(char.isdigit() for char in user_password) and not any(char.isupper() for char in user_password):
        print("Password should contain at least 1 capital letter")
    
    elif len(user_password) < 5:
        print("Password length should be greater than or equal to 5 characters")

    elif not any(char.isdigit() for char in user_password):
        print("There should be at least 1 number in the password")

    elif not any(char .isupper() for char in user_password):
        print("Password should contain at least 1 capital letter")

    elif len(user_password) >= 5 and any(char.isdigit() for char in user_password) and any(char.isupper() for char in user_password):
        print("Password is fine")
        break
    

""" 
Better solution -

while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)

"""