import sys

mountain = [int(i) for i in sys.stdin.readline().rstrip().split()]


def valid_mountain_array(mountain_int):
    up_right = True
    highland = (max(mountain_int))
    if len(mountain_int) < 3 or (
        mountain[0] == highland
            ) or (mountain[-1] == highland):
        return not up_right

    for counter in range(mountain_int.index(highland)):
        if mountain_int[counter] >= mountain_int[counter + 1]:
            up_right = False

    for counter in range(mountain_int.index(highland), len(mountain_int)-1):
        if mountain_int[counter] <= mountain_int[counter + 1]:
            up_right = False
    return up_right


print(valid_mountain_array(mountain))
