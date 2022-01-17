import getpass
import sys

def guessing_game(maximum):
    target = int(getpass.getpass('What is the target number?'))
    guess = int(input(f'Guess a number between 1 and {maximum}\n'))
    tries = 1
    while guess != target:
        tries += 1
        if guess < target:
            guess = int(input('Higher'))
        elif guess > target:
            guess = int(input('Lower'))
    print(f'Nailed it in {tries} number of tries!')

if len(sys.argv) > 1:
    guessing_game(sys.argv[1])
else:
    guessing_game('100')