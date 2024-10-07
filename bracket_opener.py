# Время посылки: 3 окт 2024, 11:14:37
# ID: 119517111

NUMBERS: str = '0123456789'


def bracket_opener(shifr: str) -> str:
    """Функция находит в тексте самую глубокую пару
    скобок и раскрывает их по правилам математики"""
    shifr = '2[a2[b]]2[c]' #abbabbcc  2[a]3[b]    2[a3[b]]
    index = 0
    newstr: str = ''
    while index < len(shifr):
        if shifr[index] in NUMBERS:
            left_brack: int = shifr.find('[')
            if shifr.find('[', left_brack+1) < shifr.find(']', left_brack+1
                ) and :
                right_brack: int = len(shifr) - shifr[-1::-1].find(']') - 1
            else:
                right_brack: int = shifr.find(']', left_brack+1)

            number = int(shifr[index:left_brack])
            #print(type(left_brack), type(right_brack), number)
            #shifr[index: right_brack+1] = number * shifr[left_brack:right_brack]
            newstr = number * shifr[left_brack+1:right_brack]
            shifr = shifr.replace(shifr[index: right_brack+1], newstr)
            print(shifr)
            index -= 1

        index += 1
    return shifr




    """
    newstr: str = ''
    left: int = len(shifr) - shifr[-1::-1].find('[') - 1
    right: int = shifr.find(']', left)
    offset: int = 1
    number: str = shifr[left-offset]

    while shifr[left-offset-1] in NUMBERS:
        number += shifr[left-offset-1]
        offset += 1

    left_half: str = shifr[0:left-offset]
    right_half: str = shifr[right+1:]
    newstr = int(number[-1::-1])*shifr[left+1:right]
    shifr = left_half + newstr + right_half
    return shifr
    """

def main() -> None:
    # shifr_input: str = input()
    # while '[' in shifr_input and ']' in shifr_input:
    #     shifr_input = bracket_opener(shifr_input)
    # print(shifr_input)
    print(bracket_opener(' '))


if __name__ == '__main__':
    main()
