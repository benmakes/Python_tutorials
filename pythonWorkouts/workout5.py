def pig_latin(s):
    if len(s) > 0:
        if s[0] in 'aeiou':
            s = s + 'way'
        else:
            s = s[1::] + s[0] + 'ay'
    return s

def pl_sentence(sentence):
    words = sentence.split()
    pl_words = []
    for word in words:
        pl_words.append(pig_latin(word))
    return ' '.join(pl_words)

print(pl_sentence('This is a test'))
