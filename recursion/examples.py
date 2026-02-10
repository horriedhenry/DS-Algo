def n_to_one(n: int):
    # print n to 1
    # base case
    if n == 0:
        return
    # print -> pre-recursion
    print(n, end=" ")
    n_to_one(n - 1)  # recursion


def one_to_n(n: int):
    # print 1 to n
    if n == 0:
        return
    # nothing before recursion
    one_to_n(n - 1)  # recursion
    print(n, end=" ")  # post-recursion


def nbr_loop(n: int):
    # 1 -> n
    for i in range(1, n + 1):
        print(i, end=" ")

    print()
    # n -> 1
    for i in range(n, 0, -1):
        print(i, end=" ")


def factorial(n: int) -> int:
    if n == 1:
        return 1
    # n -> pre-recursion add it with the return value of f(n - 1)
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    # return nth fibonacci nbr
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_n(n: int) -> int:
    # n => upper-bound
    if n == 1:
        return 1
    return n + sum_of_n(n - 1)


def sum_of_n_formula(n: int) -> int:
    return (n * (n + 1)) // 2


def fib_loop(n: int) -> int:
    # return nth fibonacci nbr
    first = 0
    second = 1
    for _ in range(n - 2):
        # internally, the rhs is executed first: also used for swapping
        # _temp1 = second
        # _temp2 = first + second
        # first = _temp1
        # second = _temp2
        first, second = second, first + second
    return second


def rev_arr(arr: list):
    front = 0
    rear = len(arr) - 1

    while front < rear:
        arr[front], arr[rear] = arr[rear], arr[front]
        front += 1
        rear -= 1


def rev_arr_rec(front: int, rear: int, arr: list):
    if front >= rear:
        return
    arr[front], arr[rear] = arr[rear], arr[front]
    rev_arr_rec(front + 1, rear - 1, arr)


def check_palindrome(s: str) -> bool:
    front = 0
    rear = len(s) - 1
    while front < rear:
        if s[front] != s[rear]:
            return False
        front += 1
        rear -= 1
    return True


def check_palindrome_rec(front: int, rear: int, s: str) -> bool:
    if s[front] != s[rear]:
        return False
    elif front >= rear:
        return True
    return check_palindrome_rec(front + 1, rear - 1, s)
