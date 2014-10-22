total = 0
counter = 0

while counter < 5:
    number = int(input("Please enter number {0} in the series: ".format(counter)))
    total = total + number
    counter = counter + 1
print("The total of the numbers you entered is {0}".format(total))
