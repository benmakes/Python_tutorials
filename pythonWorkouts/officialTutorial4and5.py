a_list = []

a_list.append(1)
a_list.extend(range(0,3))
a_list.insert(0, 6)
a_list.remove(1)
a_list.pop()
test = a_list.index(1)

#print(test)
#print(a_list)

squares = [x**2 for x in range(10)]
print(squares)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])

knights = {'galahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(knights):
    print(i, v)

questions = ['name', 'quest', 'favourite colour']
answers = ['lancelot', 'the holy grail',
 'blue']

for q, a in zip(questions, answers):
    print('What is you {0}? It is {1}.'.format(q, a))