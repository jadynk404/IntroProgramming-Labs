# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Jadyn Kennedy
# Created: 2020-02-24


x = 1
import sys

def name():
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    return first, last

def username():
    first, last = name()
    uname = str(first + "." + last)
    return uname

def checkpassword():
    x = 1
    passwd = input("create a new password: ")
    while x == 1:
       
        if len(passwd) < 8:
            x == 1
            print("The password must be at least 8 characters long.")
            passwd = str(input("Create a new password: "))
            if len(passwd) < 8:
                x = 1   
        else:
             x = 0
        while x == 0:
            if (passwd.islower()) == True or (passwd.isupper()) == True:
                x = 0
                print("This password must contain both upper and lowercase letters.")
                passwd = str(input("Please input a new password: "))
                
            if (passwd.isupper()) == False and (passwd.islower()) == False:
                x = 2
                print("This is a strong password.")

        

    return passwd
            



def main():
    uname = username().lower() #this makes sure that everything is lowercase
    passwd = checkpassword()
    print("Your account has been created. Your new email address is", uname + "@marist.edu")
    print("Your username is", uname, ".")
    print("Your password is", passwd, ".")
    sys.exit()
    

   
            


main()
