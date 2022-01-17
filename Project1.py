import turtle
t = turtle.Turtle()

def square(x):
    for _ in range(4):
        t.fd(x)
        t.rt(90)

for _ in range(10):
    square(100)
    t.rt(360/10)