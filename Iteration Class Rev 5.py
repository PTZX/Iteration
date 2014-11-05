#Paul Njenje
#29/10/2014
#Iteration Class: Revision Exercise 5

def iterate5():
    print("This program will calculate the average of a given set of numbers")
    total = 0
    while total == 0:

        print()
        num1 = int(input("First number: "))
        num2 = int(input("Second number: "))
        num3 = int(input("Third number: "))
        num4 = int(input("Fourth number: "))
        num5 = int(input("Fifth number: "))
        print()
        total = num1 + num2 + num3 + num4 + num5
        average = total / 5
        print("Total = {0}".format(total))
        print()
        
        print("Average = {0}".format(average))
        

    
