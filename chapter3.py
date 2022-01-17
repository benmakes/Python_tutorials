def print_down_from(n):
    for x in range(n, 0, -1):
        print(x)

#print_down_from(5)

def times_table(n):
    column_width = len(str(n * (n - 1))) + 1
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            print(x * y, end=' ' * (column_width - len(str(x * y))))
        print('')

#times_table(10)

def count_spaces(s):
    c = 0
    for x in s:
        if x == ' ':
            c += 1
    return c

#print(count_spaces('Abrac a d abra'))

def print_spaced(s):
    l = len(s)
    for x in s:
        print(x, end='')
        l = l - 1
        if l > 0:
            print(' ', end='')
    print('')

#print_spaced('Abracadabra')

def print_copy(s):
    print('Please type in this sentence:\n' + s)
    while input() != s:
        print('That is not the correct sentence. Please try again.')
    print('Bang on!')

#print_copy('You are on the right path just keep going!')

def ask_for_password():
    while input('Please enter the password\n') != 'please':
        pass

#ask_for_password()
import random

def guessing_game():
    n = random.randint(1, 20)
    print('Welcome to the arena of gods, mortal.')
    print('Guess a number between 1 and 20')
    guess = int(input())
    count = 0
    while guess != n:
        count += 1
        if guess < n:
            print('Higher!')
        else:
            print('Lower!')
        guess = int(input())
    print('You have true sight. Are ye truly mortal?')
    print(f'You took {count} guesses.')

guessing_game()
    
