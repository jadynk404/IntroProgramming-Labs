import math

def pi():
    n = eval(input("enter how many terms you wish to be summed: \n"))
    denominator = 1
    numerator = 4
    Sum = 0
    

    for i in range(n):
        Sum = (numerator/denominator) + Sum
        denominator = denominator + 2
        numerator = -1 * numerator
    print(Sum)
    print("This number is ", math.pi - Sum, "off from pi")
    

pi()










