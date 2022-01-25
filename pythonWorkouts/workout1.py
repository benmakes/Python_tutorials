import random

def guessing_game():
    """Players guess with input to the console a random number generated from (0 to 100) inclusive"""
    ans = random.randint(1, 100)
    cnt = 0
    guess = 0
    while guess != ans:
        cnt += 1
        guess = int(input('Guess a whole number from 1 to 100:\n'))
        if guess > ans:
            print('Too high')
        elif guess < ans:
            print('Too low')
        elif guess == ans:
            print(f'Just right. It took you {cnt} guesses.')

guessing_game()
