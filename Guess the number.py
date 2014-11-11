#Paul Njenje
#10/11/14
##Guess the number

def main():
        
    import random
    answer = random.randint(1,101)
    guess = 0
    times = 0

    upperB = 101
    lowerB = 0

    ## This program will take the users input of a number which will check if the number is
    ## and display either an invalid number 
    ## : elif
    print("Guess the number. The number will be within the range of 1-100")
    print(answer)

    while guess != answer:
        print()
        guess = int(input("Guess the number: "))
        times = times + 1

        if guess < answer and guess > lowerB:
            print("This number is too small.")
        elif guess > answer and guess < upperB:
            print("This number is too big.")
        elif guess == answer:
            print("This is the number, well done.")
        elif guess <= lowerB or guess >= upperB:
            print("Invalid number. Stick to the range 1-100")
            
    print("It took you {0} turns to Guess The Number!".format(times))
