from collections import OrderedDict, deque

data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
ordered_client_ages = OrderedDict(sorted(data, key = lambda x: x[1]))
ordered_client_ages['Alex'] = 13
print(ordered_client_ages)

clients = deque()
clients.append('Dias')
clients.append('Alina')
clients.append('Aruzhan')
clients.append('Assem')
first_client = clients.popleft()
second_client = clients.popleft()
print("First client: ", first_client)
print("Second client: ", second_client)
clients.appendleft('VIP client')
tired_client = clients.pop()
print(tired_client, " left the queue")
clients = deque(['Dias', 'Alina', 'Aruzhan', 'Assem'])
del clients[2]
print(clients)

shop = deque([1, 2, 3, 4, 5])
shop.extend([11, 12, 13, 14])
print(shop)

shop = deque([1, 2, 3, 4, 5])
shop.extendleft([11, 12, 13, 14])
print(shop)

limited = deque(maxlen = 3)
print(limited)
limited_from_list = deque([1, 2, 3, 5, 6, 8], maxlen = 3)
print(limited_from_list)

limited.extend([1, 2, 3])
limited.append(5)
print(limited)

temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]
days = deque(maxlen=7)

for temp in temps:
    days.append(temp)
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end = "; ")

dq = deque([1, 2, 3, 4, 5])
print(dq)
dq.reverse()
print(dq)
dq.rotate(2)
print(dq)
dq.rotate(-2)
print(dq)

dq = [1,2,4,2,3,1,5,4,4,4,4,4,3]
print(dq.index(4))
print(dq.count(4))
dq.clear()
print(dq)


def check(temps):
    res = OrderedDict(sorted(temps, key = lambda x: 1/ x[1]))
    return res

print(check(temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]))

from collections import OrderedDict

ratings = [
('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)
]

new_r = sorted(ratings, key = lambda x: (-x[1], x[0]))
print(new_r)

cafes = OrderedDict(new_r)

print(cafes)