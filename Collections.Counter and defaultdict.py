from collections import Counter
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
print(counter_moscow)

from collections import defaultdict

groups = defaultdict(list)
students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]

for student, group in students:
    groups[group].append(student)
    
print(groups[10])
print(groups)

from collections import deque, defaultdict

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

# print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})

def task_manager(tasks):
    d_d = defaultdict(deque)
    for number, server, priority in tasks:
        if priority == True:
            d_d[server].appendleft(number)
        else:
            d_d[server].append(number)
    return d_d

print(task_manager(tasks))


    
