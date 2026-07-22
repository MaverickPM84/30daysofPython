#Create a program that generates a password of 6 random alphanumeric characters in the range

#a-z,0-10,A-Z,special characters
"""
One small bonus tip for the future: The random module is great for general programming, 
but its generations are technically "pseudo-random" and can be predictable if someone knows the seed.
If you were generating passwords for a real, highly secure production system, 
Python provides the secrets module which is designed specifically for cryptography:

""" 


import random, string, secrets

ref_string = string.ascii_letters + string.digits + string.punctuation

# secrets.choice picks one random character securely
password = ''.join(secrets.choice(ref_string) for i in range(6)) 

print(password)

"""
alternate solution

import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)

"""


