"""Черепашка живёт на поле, расчерченном на клетки,
размер поля — X на Y.
Черепашка сидит в верхней левой клетке этого поля
с координатами 1, 1 и может двигаться или на одну клетку
вниз, или на одну клетку вправо.
На каждой клетке этого поля лежит определённое число монет.
Как вычислить максимальное число монет, которое может набрать
черепашка по пути к нижней правой клетке поля
(это клетка с координатами X, Y)?
СЕКРЕТ: Считай с конца пути!
Сначала просчитываются первая строка и первый столбец,
затем осчитываются все варианты построчно"""

from pprint import pprint

COINS = [
  [19, 8,  3,  12, 7],
  [0,  7,  16, 13,  14],
  [15, 18, 1,  17, 2],
  [3,  11, 6,  20, 13],
  [1, 63,  0,  15, 9]
]
print('Поле:')
pprint(COINS)
# for i in range(len(COINS)):
#     for j in range(len(COINS[i])):
#         print(COINS[i][j], '\t', end='')
#     print()
M = 5
bestway = [[0] * M for i in range(M)]
way = [['.'] * M for i in range(M)]

for i in range(M):
    for j in range(M):
        if i == 0 and j == 0:
            bestway[0][0] = COINS[0][0]
        elif i == 0:
            bestway[0][j] = bestway[0][j-1] + COINS[0][j]
        elif j == 0:
            bestway[i][0] = bestway[i-1][0] + COINS[i][0]
        else:
            bestway[i][j] = max(bestway[i-1][j], bestway[i][j-1]) + COINS[i][j]

print('\nСумма монеток:\n')
pprint(bestway)

i, j = M-1, M-1

way[i][j] = 'Х'
while i > 0 and j > 0:
    if i > 0 and j > 0:
        if bestway[i-1][j] >= bestway[i][j-1]:
            way[i-1][j] = 'V'
            i -= 1
        else:
            way[i][j-1] = '->'
            j -= 1
    if i == 0:
        for num in range(j):
            way[0][num] = '->'
            j = 0
    if j == 0:
        for num in range(i):
            way[num][0] = 'V'
            i = 0
print()
# print('\nПуть:\n')
# for i in range(len(bestway)):
#     print('\t'.join(way[i]))
pprint(way)
