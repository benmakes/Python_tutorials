import math
def rounding(n):
    c = math.ceil(n)
    f = math.floor(n)
    if c - n <= n - f:
        return c
    else:
        return f

#print(rounding(2.4))

def midpoint(a,b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 + x1) / 2, (y2 + y1) / 2)

def parts(n):
    whole = int(n)
    fractional = n - whole
    return (whole, fractional)

#print(parts(3.7), parts(3.2), parts(-3.2), parts(-3.7))

def star(x):
    i = math.floor(x * 50)
    if i == 50: i = 49
    print(' ' * (i - 1) + '*')

def plot(f, a, b, dy):
    pos = a
    while pos <= b:
        star(f(pos))
        pos += dy

plot(math.sin, 0, math.pi, math.pi/20)