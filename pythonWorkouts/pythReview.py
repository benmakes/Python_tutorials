

numbers = [1,2,3,4]
num_sum = 0
for num in numbers:
    num_sum += num

users = {'Hans': 'active', 'Tim': 'inactive', 'Al': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

numbers.reverse()

print(numbers)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

basket.add('grape')
print(basket)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print(key, value)

for ind, value in enumerate(['tic', 'tac', 'toe']):
    print(ind, value)

class Complex():
    def __init__(self, realp, imagp):
        self.r = realp
        self.i = imagp
        self.l = [realp, imagp]

myComplex = Complex(1,2)
print(myComplex.r, myComplex.i, myComplex.l)

#recursion example
def recusive_sum(n):
    if n == 0:
        return n
    return n + recusive_sum(n-1)

print(recusive_sum(10))