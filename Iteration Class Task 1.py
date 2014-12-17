#Paul Njenje
#22/10/14
#Iteration Class Exercise Task 1

### program to prompt for 8 numbers and report the total to the user
##num1 = int(input('Enter number 1: '))
##num2 = int(input('Enter number 2: '))
##num3 = int(input('Enter number 3: '))
##num4 = int(input('Enter number 4: '))
##num5 = int(input('Enter number 5: '))
##num6 = int(input('Enter number 6: '))
##num7 = int(input('Enter number 7: '))
##num8 = int(input('Enter number 8: '))
##
##total = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
##
##print('The total is {0}'.format(total))
num = 0
total = 0

for count in range(1,9):
    num = int(input("Enter number {0}: ".format(count)))
    total = num + total
    print()

print("Equals {0}".format(total))


