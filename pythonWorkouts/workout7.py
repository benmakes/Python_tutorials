def ubbi_dubbi(word):
    """Given a word with no spaces, inserts ub before each vowel"""
    ud_letters = []
    for letter in word:
        if letter in 'aeiou':
            ud_letters.append('ub'+letter)
        else:
            ud_letters.append(letter)
    return ''.join(ud_letters)

print(ubbi_dubbi('python'))