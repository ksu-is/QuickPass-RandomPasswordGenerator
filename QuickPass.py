import random 
import string 

print("Welcome to QuickPass!")

while True:
    try:           
        num_passwords = int(input("Amount of passwords to generate: "))
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
          
for i in range(num_passwords):
    randomchar = random.choice(characterList)
    password.append(randomchar)

print(password)
