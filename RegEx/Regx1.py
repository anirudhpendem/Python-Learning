
import re

def passwd():

    regx =r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%^&*?~])[A-Za-z\d@!#$%^&*?~]{8,}$"

    password = input("Enter the password which must have Atleast (One Upper & Lower case,One Special character,One Digit) :")
    
    match = re.compile(regx)
                 
    result= re.search(match, password)

    if result:
        print("Password is valid.")
    else:
        print("Password invalid !!")

passwd()
