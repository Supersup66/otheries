# Время посылки:20 сен 2024, 15:25:43
# ID: 118378926

def min_platform(robots: list[int], limit: int) -> int:
    """
    Функция определит минимальное количество транспортных платформ,
    необходимое для перевозки всех роботов, описанных в массиве
    """
    left_point = 0
    right_point = len(robots) - 1
    counter_platform = 0
    robots = sorted(robots, reverse=True)
    while left_point <= right_point:
        if limit >= robots[left_point] + robots[right_point]:
            right_point -= 1
        counter_platform += 1
        left_point += 1
    return counter_platform


def main():
    robots = [int(i) for i in input().split()]
    limit = int(input())
    print(min_platform(robots, limit))


if __name__ == '__main__':
    main()
