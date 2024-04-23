import random 
import string 

print("Welcome to QuickPass!")

while True:
    try:           
        num_passwords = int(input("Amount of passwords to generate: "))
        if num_passwords <= 0: 
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
                  
characterList = ''

while True:
    choice = int(input("Pick a number "))
    if(choice == 1):
        characterList += string.digits
    elif(choice == 2): 
        characterList += string.ascii_letters
    elif(choice == 3):      
        characterList += string.punctuation
    elif(choice == 4): 
        break 
    else: 
        print("Pick a valid option to continue!")
              
password = []
          
<<<<<<< HEAD
def main(): 
    print("Welcome to QuickPass!")

    while True:
        try:           
            amount = int(input("Amount of passwords to generate: "))
            if amount <= 0: 
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
                  
print('''Choose character set for password:
          1. Digits
          2. Letters
          3. Punctuation
          4. Exit''')

for i in range(amount):
=======
for i in range(num_passwords):
>>>>>>> 9c6b3aa6f82479074c3dff635c3c2fad63b0e612
    randomchar = random.choice(characterList)
    password.append(randomchar)

print(password)
