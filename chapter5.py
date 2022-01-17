def sorted_words(s):
    return sorted(s.split())

def sorted_words2(s):
    l = s.split()
    l.sort()
    return l

def setify(l):
    l2 = []
    for x in l:
        if x not in l2:
            l2.append(x)
    return l2

def histogram(l):
    unique = sorted(setify(l))
    for x in unique:
        print(f'{x} appears {l.count(x)} times.')
    
#histogram([1,1,1,2,2,2,3,4,5,6,6])

def strip_leading_spaces(l):
    while len(l) > 0 and l[0] == ' ':
        del l[0]

def remove_spaces(s):
    l = list(s)
    strip_leading_spaces(l)
    l.reverse()
    strip_leading_spaces(l)
    l.reverse()
    return ''.join(l)

#print(remove_spaces('           abcde  e      '))

def remove_spaces_abuse(s):
    l = ' '.join(s.split())
    return l

def clip(x):
    if x > 10:
        return 10
    elif x < 1:
        return 1
    else:
        return x

def clip_list(l):
    return list(map(clip, l))

def palindromic(s):
    return s == s[::-1]

def palind_filter(l):
    return list(filter(palindromic, l))

#print(palind_filter(['abcde', 'abcba', 'abba']))

def palindromic_range(n1,n2):
    the_range = range(n1,n2)
    l = list(map(str, list(the_range)))
    return list(map(int, palind_filter(l)))

print(palindromic_range(1000,10000))

def clip_list_comprehension(l):
    return [clip(x) for x in l]

def palindromic_range2(n1,n2):
    strings = map(str, range(n1, n2))
    return [int(x) for x in strings if palindromic(x)]

print(palindromic_range2(1000, 10000))

