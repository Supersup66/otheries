"""Хер его знает, как у меня это получилось,
но оно работает с линейной сложностью.
программа определяет максимальное количество блоков
для сортировки слиянием блоков
"""


arr = [int(x) for x in ('0 1 3 2'.split())]
arr_len = len(arr)
lower, higher = 0, 0
counter = 0
for i in range(arr_len):
    higher = max(higher, arr[i])
    if lower in arr[:i+1] and higher == len(arr[:i+1])-1:
        print(arr[lower:i+1])
        counter += 1
        lower = higher
print(counter)
