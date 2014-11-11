#Paul Njenje
#29/10/2014
#Iteration Class: Revision Exercise 5

def iterate5():
    #This program will average a set of numbers.
    #ask the user for the number of intergers
    
    print("This program will calculate the average of a given set of numbers")
    total = 0
    numSet = int(input("How many numbers do you want to average (2-5): "))
        
    if numSet < 6 and numSet > 2:
        print()
        num1 = int(input("1st number: "))
        num2 = int(input("2nd number: "))
        num3 = int(input("3rd number: "))
        num4 = int(input("4th number: "))
        num5 = int(input("5th number: "))
        print()
        total = (num1+num2+num3+num4+num5)

        average = total / numbSet
        print("Total = {0}".format(total))
        print()
        print("Average = {0}".format(average))

