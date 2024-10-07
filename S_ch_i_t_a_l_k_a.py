"""Ебись считалка вороным конем!
зато работает"""

members = 500
rounds = 500
line = [member for member in range(members)]
current_ind = 0
while len(line) > 1:
    #print(f'{line} Считает номер {current_ind}')
    move = rounds % (len(line)) - 1
    # if rounds == len(line):
    #     current_ind = len(line) - 1
    # else:
    current_ind += move
    if current_ind > len(line) - 1:
        current_ind -= len(line)
    #print(f'Выбыл: {line[current_ind]}')
    line.pop(current_ind)
    if current_ind < 0:
        current_ind = 0

print(line[0])