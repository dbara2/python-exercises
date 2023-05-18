##program designed to create a random number and have the user guess it until the get it right.
import random
random_number = random.randint(0,10)
"""for i in range(10):
    print(random_number)"""

users_guess = int(input('Guess a number between 0 and 10\n'))


'''if users_guess < random_number:
    print('too low')
    if users_guess > random_number:
        print('too high')
    else:
        users_guess == random_number
        print("You got it!")'''

while users_guess != random_number:
    if users_guess > random_number:
        print('too high')
        users_guess = int(input('Try again, guess a number between 0 and 10\n'))
    elif users_guess < random_number:
        print('too low')
        users_guess = int(input('Try again, guess a number between 0 and 10\n'))
    else:
        break
print('you got it!')


