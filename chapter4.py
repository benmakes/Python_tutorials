l = [2, 3, 4, 5]

def first(l):
    return l[0]

#print(first(l))

def last(l):
    return l[-1]

#print(last(l))

def reversed_list(l):
    l2 = []
    for x in range((len(l) - 1), -1, -1):
        l2.append(l[x])
    return l2

#print(reversed_list(l))

def minmax(l):
    minimum = l[0]
    maximum = l[0]
    for x in l:
        if x > maximum:
            maximum = x
        elif x < minimum:
            minimum = x
    print(f'The list minimum is {maximum}')
    print(f'The list maximum is {minimum}')

#minmax(l)

def evens(l):
    l2 = []
    for i, elt in enumerate(l):
        if (i % 2) == 0:
            l2.append(elt)
    return l2

def evensEasy(l):
    return l[::2]

#print(evens(l))

def reversed_easy(l):
    return l[::-2]

def setify(l):
    l2 = []
    for x in l:
        if x not in l2:
            l2.append(x)
    return l2

# print(setify([1,2,3,1,2,3]))

def histogram(l):
    l2 = setify(l)
    l3 = []
    for x in l2:
        l3.append(l.count(x))
        print(f'{x} appears {l.count(x)} times')

#histogram([1,2,2,2,3,3,3,3,3,5,6,7,7])

def string_tester(s, w1, w2, w3):
    if w1 in s:
        print(f'{w1} is in {s}')
    if w2 in s:
        print(f'{w2} is in {s}')
    if w3 in s:
        print(f'{w3} is in {s}')

#string_tester('I am just a guy that loves the flow of trying hard', 'guy', 'easy', 'flow')

def copy_list(l):
    l2 = []
    for x in l:
        l2.append(x)
    return l2

def copy_list_easy(l):
    return l[:]

def remove_list_item(l, x):
    l2 = copy_list(l)
    l2.remove(x)
    return l2

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rotate(n, a):
    return a[n:] + a[:n]

def encode(text, cipher):
    out = ''
    for x in text:
        if x == ' ': 
            out = out + ' '
        else: 
            out = out + cipher[alph.index(x)]
    return out

def decode(text, cipher):
    out = ''
    for x in text:
        if x == ' ': 
            out = out + ' '
        else:
            out = out + alph[cipher.index(x)]
    return out

#secret_message = encode('EVERY DAY IS A CLIMBING DAY WHEN YOU HAVE A REMOTE JOB', rotate(3, alph))
#print(decode(secret_message, rotate(3, alph)))

import random

def check_code_guess(code, guess):
    code = code.copy()
    guess = guess.copy()
    correct = 0
    incorrect_place = 0
    #first pass, correct number in correct place
    for x in range(0, 4):
        if guess[x] == code[x]:
            correct += 1
            guess[x] = -1
            code[x] = -1
    for x in range(0,4):
        if guess[x] > -1:
            if guess[x] in code:
                incorrect_place = incorrect_place + 1
                code[code.index(guess[x])] = -1
    print(f'Correct number in correct place: {correct}')
    print(f'Correct number in incorrect place: {incorrect_place}')
    return code == guess

def code_guesser():
    a = random.randint(1,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)
    code = [a, b, c, d]
    tries = 1
    i = input('Guess the code with 4 digits: ')
    guess = [int(i[0]), int(i[1]), int(i[2]), int(i[3])]
    while guess != code:
        if check_code_guess(code, guess):
            pass
        else:
            tries = tries + 1
            i = input('Guess the code with 4 digits: ')
            guess = [int(i[0]), int(i[1]), int(i[2]), int(i[3])]
    print(f'Nailed it with {tries} guesses')

code_guesser()

