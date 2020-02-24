# CMPT 120 Intro to Programming
# Lab #5 - Working with Strings and Functions
# Author: Jadyn Kennedy
# Created: 2020-02-24
x = 1
import sys
def main():
    while x == 1:
        first = input("Please enter your first name: ")
        last = input("Please enter your last name: ")

        uname = first + "." + last

        passwd = input("create a new password: ")
    
        if len(passwd) < 8:
            x == 1
            print("The password must be at least 8 characters long.")
            passwd = input("Create a new password: ")
            if len(passwd) < 8:
                return loop
            else:
                x == 0
            print("This is a strong password.")
            print("Your account has been created. Your new email address is", uname + "@marist.edu")
            sys.exit()

        else:
            x == 0
            print("This is a strong password.")
            print("Your account has been created. Your new email address is", uname + "@marist.edu")
            sys.exit()
            


main()
