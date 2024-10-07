def encrypted_instructions(instructions: str) -> str:
    """Функция расшифровывает сжатые сообщения и возвращает полные."""
    open_bracket = '['
    close_bracket = ']'
    chars = ''
    ratio = ''
    stack = []

    for i in range(len(instructions)):
        if instructions[i].isalpha():
            chars += (instructions[i])
        elif instructions[i].isnumeric():
            ratio += (instructions[i])
        elif instructions[i] == open_bracket:
            stack.append(chars)
            stack.append(ratio)
            chars = ''
            ratio = ''
        elif instructions[i] == close_bracket:
            chars *= int(stack[-1])
            stack.pop()
            chars = stack[-1] + chars
            stack.pop()

    return chars


def main() -> None:
    """Основная функция программы."""
    instructions: str = input()
    print(encrypted_instructions(instructions))


if __name__ == '__main__':
    main()
