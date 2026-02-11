# keep adding b to b "a" times; add "b" a times
def mul_a(a: int, b: int):
    if a == 0:
        return 0
    return mul_a(a - 1, b) + b


# keep adding a to a b times; add "a" b times
def mul_b(a: int, b: int):
    if b == 0:
        return 0

    return mul_b(a, b - 1) + a


# mul_a or mul_b does not work for negative numbers
# if a is -ve and b is +ve the result should be -ve
# if a is +ve and b is -ve the result should be -ve
# if a is -ve and b is -ve the result should be +ve
def mul_c(a: int, b: int):
    # TODO - Implement later looked at solution.. kind of understood.. do it later.. to be sure i did
    pass


a, b = 2, 5

print(mul_a(a, b))
