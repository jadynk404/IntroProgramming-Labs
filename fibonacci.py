import math
n = int(input("Please input a number 'n'\n"))
def fibonacci(n):
    
    Phi = ((1+5**.5)/2)
    phi = ((1-5**.5)/2)
 
    return (((Phi)**n)-(phi)**(n))/(5**(.5))

print(int(fibonacci(n)))

#citation: found fibonacci sequence formula online, defined Phi variables to solve


