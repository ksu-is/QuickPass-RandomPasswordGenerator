import random 
          
Numbers = '0123456789'
Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Punctuation = '~`!@#$%^&*+=:;?"

def main(): 
    print("Welcome to QuickPass!")

    while True:
        try:           
            

amount = int(input("Amount of passwords to generate: "))

length = int(input("Enter desired password length: "))

print('''Choose character set for password :
          1. Numbers
          2. Letters
          3. Punctuation
          4. Exit''')

