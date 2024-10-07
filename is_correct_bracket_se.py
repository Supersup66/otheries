"""Поверяет последовательость скобок на правильность
количество открытых и закрытых скобок должно совпадать"""


def is_correct_bracket_seq(str_seq):
    if str_seq == '':
        return True
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    opening = pairs.keys()
    stack = []
    for char in str_seq:
        if char in opening:
            stack.append(char)
        else:
            if stack > [] and char in pairs[stack[-1]]:
                stack.pop()
            else:
                return False
    return stack == []


sequence = input()
print(is_correct_bracket_seq(sequence))
