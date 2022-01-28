from asyncio.windows_events import NULL


def firstlast(sequence):
    """Return the first and last elements of a sequence, whether the type be string, list, or tuple"""
    try:
        fl = sequence[:1] + sequence[-1:]
        return fl
    except TypeError:
        print('The wrong data type was passed to the function firstlast()')
        return sequence

#print(firstlast('abcde'))
#print(firstlast(['1', '2', '3', '4', '5']))
#print(firstlast((1,2,3,4,5)))

print(firstlast({1:'abcde'}))