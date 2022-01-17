def list_sum(l):
    total = 0
    for x in l:
        try:
            total += int(x)
        except ValueError:
            pass
    return total

def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None

def not_none(x):
    return x is not None

def list_sum2(l):
    return sum(filter(not_none, map(safe_int, l)))

def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

def dict_take(a, b):
    c = {}
    for k, v in a.items():
        try:
            c[k] = b[k]
        except KeyError:
            pass
    return c

def safe_union(a, b):
    c = {}
    for k, v in a.items():
        c[k] = v
    for k, v in b.items():
        if k in c:
            raise KeyError
        else:
            c[k] = v
    return c

def add_exception(s, k):
    if k in s:
        raise KeyError
    else:
        s.add(k)


