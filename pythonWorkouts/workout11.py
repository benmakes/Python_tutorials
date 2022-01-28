import operator

def alphabetize_names(list_of_dicts):
    """Don't really want to do this workout... but I will look up sort with keys and operator.itemgetter() which returns a function"""
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))

