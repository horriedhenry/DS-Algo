import math


def two_crystal_balls_for(arr):
    # arr = [False] throws error for this
    # works well for a filled array, arr[False] * 10 + [True] * 10
    length = len(arr)
    jump_amount = math.floor(math.sqrt(length))

    for i in range(jump_amount, length, jump_amount):
        if arr[i]:
            break

    i -= jump_amount

    for _ in range(jump_amount):
        if i >= length:
            break
        elif arr[i]:
            return i
        i += 1

    return None


def two_crystals(arr):
    length = len(arr)
    jump_amount = math.floor(math.sqrt(length))

    i = jump_amount
    while i < length:
        if arr[i]:
            break
        i += jump_amount

    i -= jump_amount

    for _ in range(jump_amount):
        if i >= length:
            break
        elif arr[i]:
            return i
        i += 1

    return None


arr = [False]

break_pos = two_crystals(arr)
print(break_pos)
