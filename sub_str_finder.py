"""Поиск подстроки из неповторяющихся симоволов"""


"""Мой вариант в 2 цикла
vvod = input()
vvod = '12345267'
result = 0
for index in range(len(vvod)):
    seq_slice = ''
    for seq in range(index, len(vvod)):
        if vvod[seq] not in seq_slice:
            seq_slice += vvod[seq]
        else:
            break
    print(seq_slice)
    result = max(len(seq_slice), result)
print(result)
"""


'''Чужой вариант. При встрече повторного симовла он не сбрасывает
всю последовательность, а отрезает слева
в месте первой встречи такого символа
'''
vvod = '12345267'
res = 0
seq_slice = ''
for char in vvod:
    if char not in seq_slice:
        seq_slice += char
        res = max(res, len(seq_slice))
    else:
        cut = seq_slice.index(char)
        seq_slice = seq_slice[cut + 1:] + char
    print(seq_slice, res)
print(res)
