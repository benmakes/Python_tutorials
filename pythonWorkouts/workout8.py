def strsort(a_str):
    """Sorts a string by unicode value and returns the sorted string"""
    char_list = sorted(a_str)
    return ''.join(char_list)

print(strsort('bedafe'))
print(strsort('cda cba'))