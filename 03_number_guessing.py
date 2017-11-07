import random

# rightNumber = 6
rightNumber = random.randint(0, 100)

while True:
    numberString = input('Guess a number: ')
    numberInt = int(numberString)

    if rightNumber == numberInt:
        print('Correct!')
    elif rightNumber > numberInt:
        print('Smaller...')
    else rightNumber < numberInt:
        print('Bigger!')