def pig_latin(s):
    if len(s) > 0:
        if s[0] in 'aeiou':
            s = s + 'way'
        else:
            s = s[1::] + s[0] + 'ay'
    return s

print(pig_latin('python'))
print(pig_latin('onto'))
print(pig_latin(''))
