import math


def count_dig(n: int) -> int:
    # time complexity O(logN) + 1, don't get why it's logN : TODO :- learn why
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count


def count_dig_optimal(n: int) -> int:
    # Time complexity : O(1)
    # the loop version is safer, i don't get this log stuff rn: TODO :- learn why
    """
    The logarithmic base 10 of a positive integers gives the number of digits in n. We add 1 to the result to ensure that the count is correct even for numbers that are powers of 10.
    We cast the result to an integer to ensure that any fractional part is discarded giving the exact count of digits.
    """
    return int(math.log10(n) + 1)


def sum_digits(n: int) -> int:
    res = 0
    while n > 0:
        last_digit = n % 10
        res += last_digit
        n = n // 10
    return res


print(count_dig(5105))
