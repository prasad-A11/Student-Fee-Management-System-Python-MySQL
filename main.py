from admin import admin  # importing admin function from the admin.py files.......
from admin import student

#  this is main heading.....
print(" choose yr role to proceeed :--  ")
print("1. admin")
print("2. student")
option = int(input("Enter your role to access option 1 or 2.........."))  # based on the given input it's going to be accses

if option == 1:
    print("your going to access admin role..1..")        # user input 
    admin()                                              # call function from admin file  
    
if option == 2:
    print("your going to access students role....2.")  
    student()