class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

#Class instantiation example
x1 = MyClass()

class Complex:
    """A complex number class example"""
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x2 = Complex(3.0, -4.5)
print((x2.r, x2.i))

x1.counter = 1
while x1.counter < 10:
    x1.counter = x1.counter * 2
print(x1.counter)
del x1.counter

#mutable objects such as lists and dictionaries can be mistakenly shared if not implemented properly between classes

class Dog:
    """A class about dogs to display instantiation"""
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

#At 9.4 Random Remarks

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

#Pause at 9.6 Private Variables

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char)