"""будет принимать на вход массив для сортировки
и массив-шаблон, в соответствии с которым должна
быть выполнена сортировка;
вернёт массив, отсортированный в соответствии с шаблоном."""


len_num = int('7')
arrived = [int(x) for x in ('8 4 9 3 10 3 3'.split())]
len_sample = int('1')
sample = [int(x) for x in ('8'.split())]
# len_num = int(input())
# arrived = [int(x) for x in (input().split())]
# len_sample = int(input())
# sample = [int(x) for x in (input().split())]

sorted_index = 0
for sam_num in sample:
    for i in range(len_num):
        if arrived[i] == sam_num:
            arrived[i], arrived[sorted_index] = arrived[
                sorted_index], arrived[i]
            sorted_index += 1
arrived[sorted_index:] = sorted(arrived[sorted_index:])
print(' '.join(map(str, arrived)))
