import random 
          
Numbers = '0123456789'
Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Punctuation = '~`!@#$%^&*+=:;?"

def main(): 
    print("Welcome to QuickPass!")

    while True:
        try:           
            amount = int(input("Amount of passwords to generate: "))
            if amount <= 0: 
                print("Must enter a positive integer to continue."
            else:           
                 break
        except ValueError:
            print("Must enter valid integer to continue.")
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length <= 0:
                 print("Must enter a positive integer to continue."
            else:           
                 break
        except ValueError:
            print("Must enter valid integer to continue.")
                  
print('''Choose character set for password:
          1. Numbers
          2. Letters
          3. Punctuation
          4. Exit''')

print('\nHere are your passwords: ')

for pwd in range(amount):
    password = ''
    for c in range(length):
        passwords += random.choice(Numbers, Letters, Punctuation)
    print(passwords)
