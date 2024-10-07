# Время посылки: 4 окт 2024, 11:50:06
# ID: 119602517

def bracket_opener(shifr: str) -> str:
    """Функция находит в тексте самую глубокую пару
    скобок и раскрывает их по правилам математики"""

    index: int = 0
    while not shifr.isalpha():
        # Пока вся строка не будет только из букв
        # Находим число, и 2 скобки после него
        if shifr[index].isnumeric():
            left_brack: int = shifr.find('[', index+1)
            right_brack: int = shifr.find(']', left_brack+1)
            # Если между скобок только буквы,
            # раскрываем скобки и вставляем обратно
            if shifr[left_brack+1:right_brack].isalpha():
                number = int(shifr[index:left_brack])
                newstr = number * shifr[left_brack+1:right_brack]
                shifr = shifr.replace(shifr[index: right_brack+1], newstr)
                # Если замена произведена, начинаем поиск заново
                index = 0
                continue

        index += 1
    return shifr


def main() -> None:
    print(bracket_opener(input()))


if __name__ == '__main__':
    main()
