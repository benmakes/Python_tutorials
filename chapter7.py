a = 1
b = 2
b, a = (a, b)

def unzip(d):
    key_list = []
    value_list = []
    for k, v in d.items():
        key_list.append(k)
        value_list.append(v)
    return (key_list, value_list)

def dict_of_keys_and_values(ks, vs):
    d = {}
    for x in range(0, len(ks)):
        d[ks[x]] = vs[x]
    return d

def union(a, b):
    u = {}
    for x in b: u[x] = b[x]
    for x in a: u[x] = a[x]
    return u

def remove_zeroes(l):
    for x in range(len(l)-1, -1, -1):
        if l[x] == 0: del l[x]
    return l

def better_remove_zeroes(l):
    while 0 in l:
        l.remove(0)

#l = [1, 0, 0, 0, 1]
#better_remove_zeroes(l)
#print(l)

def reverse_dict(d):
    return {v:k for k, v in d.items()}

def letter_set(l):
    letters = set()
    for x in l:
        letters = letters | set(x)
    return letters

def letters_not_used(l):
    alphabet_set = set('qwertyuiopasdfghjklzxcvbnm')
    return alphabet_set - letter_set(l)

def sum_all(t):
    if type(t) == int:
        return int
    else:
        total = 0
        for x in t:
            total += sum_all(x)
        return total


