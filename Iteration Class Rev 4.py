#Paul Njenje
#29/10/2014
#Iteration Class: Revision Exercise 4

def iterate4():
    number = 0
    while number > 20 or number < 9:

        print()
        number = int(input("Enter a number between 10 and 20: "))
        if number < 9:
            print("Invalid Value - Enter a bigger number")
        elif number > 20:
            print("Invalid Value - Enter a smaller number")
        else:
            print("Well Done! Here is kirby ༼ つ ◕_◕ ༽つ. Give him a hug... he looks kinda sad")
            
