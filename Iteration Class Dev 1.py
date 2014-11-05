##Paul Njenje
##05/11/14
##Iteration Class Dev Exercise 1
n = int(input('Enter an integer >= 0: '))
fact = 1
for i in range(2, n + 1):
    fact = fact * i
print(str(n) + ' factorial is ' + str(fact))
