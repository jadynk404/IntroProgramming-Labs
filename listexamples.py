colors = ["BLUE", "NAVY", "GREEN", "YELLOW", "IVORY", "MAROON"]

def showTitle():
    print("Color Preference Evaluator")
    
def promptForColor():
    color = input("Please input a color: ")
    color = color.strip()
    color = color.upper()
    return color

def praiseUser():
    print("I like this color too. You chose nicely.")
    
def ridiculeUser():
    print("What an awful color. Try to use better taste when picking next time.")
    
def confirmColor():
    x = 1
    color = promptForColor()
    while x == 1:
        checktext = "You entered {}. Is this  correct? (Y/N)\n".format(color)
        confirm = input(checktext)
        confirm = confirm.lower()
        if confirm[0] == "y":
            x = 0
        elif confirm[0] == "n":
            x = 1
        else:
            x = 1
    return color

def containsElement():
    x = 2
    color = confirmColor()
    while x == 2:
        if color == colors[0] or color == colors[1] or color == colors[2] or color == colors[3] or color == colors[4] or color == colors[5]:
            x = 0
            praiseUser()
        else:
            x = 0
            ridiculeUser()

def main():
    showTitle()
    containsElement()
    
main()
        
