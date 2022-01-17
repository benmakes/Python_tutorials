def print_powers(n):
    f = open('powers.txt', 'w')
    for x in range(1, n):
        print(f'{x:5d} {x ** 2:5d} {x ** 3:5d} {x ** 4:5d}', file=f)
    f.close()

def print_powers2(n):
    with open('powers.txt', 'w') as f:
        for x in range(1, n):
            print(str(x).rjust(5), str(x**2).rjust(5), str(x**3).rjust(5), str(x**4).rjust(5), file=f)

#print_powers2(6)

def print_list(l):
    length = len(l)
    print('[', end='')
    for x in l:
        print(x, end='')
        length -= 1
        if length > 0:
            print(', ', end='')
    print(']')

#print_list([1, 2, 3])

def names_to_write_to_file(filename):
    with open(filename, 'w') as f:
        name = 'not empty'
        while name != '':
            name = input('Title, forename and surname, please: ')
            if name != '':
                words = name.split()
                print(words[2], words[1], words[0], sep=', ', file=f)

#names_to_write_to_file('names.txt')

def number_found(sentences, word, filename):
    n = 0
    with open(filename, 'w') as f:
        for s in sentences:
            n += 1
            p = s.find(word)
            if p == -1:
                print(f'{word} not found in sentence {n}')
            else:
                print(f'{word} found at position {p} in sentence {n}')


    


    