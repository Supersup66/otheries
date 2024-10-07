"""Внизу закооментирована первая версия с квадратичной сложностью -
на вводных списках по 10000 элементов - работала больше секунды
Здесь при любых вводных - всего 21000 итераций - работает 40мс """
len_order = int('10')
ordered = [int(x) for x in ('8 5 5 8 6 9 8 2 4 7'.split())]
len_arr = int('8')
arrived = [int(x) for x in ('9 8 1 1 1 5 10 8'.split())]
"""Требование заказчика считается выполненным
если он получит образец, вес которого равен
заказанному или превышает заказанный вес.
"""
counter = 0
order_sorted = [0] * 1001
arrived_sorted = [0] * 1001
for i in ordered:
    order_sorted[i] += 1
for i in arrived:
    arrived_sorted[i] += 1
# print(f' Прибыло: \n {arrived_sorted}')
# print(f' Заказано: \n {order_sorted}')
storage = 0
for i in range(len(order_sorted)-1, 0, -1):
    if arrived_sorted[i] > 0:
        storage += arrived_sorted[i]
    while order_sorted[i] > 0 and storage > 0:
        storage -= 1
        order_sorted[i] -= 1
        counter += 1
# print(f'Выполнено: {counter} заказов.')
print(counter)

"""
for order in ordered:
    for i in range(len(arrived)):
        if arrived[i] >= order:
            counter += 1
            arrived.pop(i)
            break
print(counter)
"""
