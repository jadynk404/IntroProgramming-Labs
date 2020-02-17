def main():
    print("Python Guessing Game")
    x=1

    while x==1:
        y = input("I'm thinking of an animal. Can you guess what it is?\n")
        c = "python"
        if c == y:
            x = 0
            print("Congratulations! You won!")
        else:
            print("Sorry. That's not it. Try Again!\n")

main()
        
