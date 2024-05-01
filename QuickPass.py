import random 
import string 
 
print("Welcome to QuickPass!")

while True:
    try:           
        num_passwords = int(input("Enter the amount of passwords to generate: "))
        if num_passwords <= 0: 
            print("Must enter a positive integer to continue.")
        else:
            break
    except ValueError:
            print("Must enter valid integer to continue.")
              
while True:
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Must enter a positive integer to continue.")
        else:           
            break
    except ValueError:
         print("Must enter valid integer to continue.")

print('''Choose character set for password from these: 
    1. Digits
    2. Letters
    3. Punctuation
    4. Exit''')
                  
characterList = ""
    
while True:
    choice = int(input("Pick a number "))
    if choice == '1':
        characterList += string.digits
    elif choice == '2': 
        characterList += string.ascii_letters
    elif choice == '3':      
        characterList += string.punctuation
    elif choice == '4': 
        break 
    else: 
        print("Pick a valid option to continue!")
              
for pwd in range(num_passwords):
    password = '' 
    for c in range(length):
        passwords += random.choice(characterList)
    print("Here are your passwords:", password)
    
