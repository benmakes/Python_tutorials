import string

def string_is_integer(s):
    is_integer = True
    if len(s) == 0:
        is_integer = False
    for x in s:
        if x not in string.digits: is_integer = False
    return is_integer

import getpass

def guessing_game():
    target = int(getpass.getpass('What is the target number?'))
    guess = int(input('Guess a number between 1 and 100\n'))
    tries = 1
    while guess != target:
        tries += 1
        if guess < target:
            guess = int(input('Higher'))
        elif guess > target:
            guess = int(input('Lower'))
    print(f'Nailed it in {tries} number of tries!')

import statistics

def get_stats(l):
    return (statistics.median(l), statistics.mode(l), statistics.mean(l))

import time

def reaction_test():
    print('Ready? Press Enter when you see ENTER')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('ENTER')
    t = time.time()
    enter = input()
    t2 = time.time()
    print(f'Your reaction time was {t2 - t} seconds')

reaction_test()