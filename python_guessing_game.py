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
            p = input("Sorry. That's not it. Try Again?\n")
            
            if p[0] == "y":
                x = 1    
            else:
                x = 0
                print("Ok. Looks like someone's a sore loser. Seeya!")
                
                
            

        

main()
        
