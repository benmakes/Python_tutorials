def mysum(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print(mysum(*[10, 20, 30]))