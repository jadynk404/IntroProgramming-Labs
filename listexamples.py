colors = ["PURPLE", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"]

def showTitle():
    print("Color Preference Evaluator")
    
def promptForColor():
    color = input("Please input a color: ")
    color = color.strip()
    return color

def praiseUser():
    print("I love this color too. Nice choice.")
    
def ridiculeUser():
    print("Really? This color sucks. Why would I include it in my list?")
    
def confirmColor():
    x = 1
    color = promptForColor()
    color = color.upper()
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
    color = color.upper()
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
        
