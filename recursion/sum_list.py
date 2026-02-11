def sum_odd(li: list) -> int:
    sum = 0
    for num in li:
        sum += num if num % 2 != 0 else 0
        # if num % 2 != 0:
        #     sum += num
    return sum


def sum_of_odds(idx: int, li: list):
    if idx >= len(li):
        return 0

    value = li[idx] if li[idx] % 2 != 0 else 0

    return sum_of_odds(idx + 1, li) + value
    # return sum_of_odds(idx + 1, li) + (li[idx] if li[idx] % 2 != 0 else 0)


# product is different: no product = 0; if one rec-call returns 0 the entire result will be zero
def product_of_even_nbrs_rec(idx: int, li: list):
    # Can't wrap my head around this problem.. it's really tough rn
    # li = [1, 7, 3]  # 0 => no even number so product is 0
    # li = [1, 2, 3, 4, 5] # 8
    # li = [-8, 3, 2] # -16
    # li = [6,0] # 0
    # li = [] # 0
    pass


li = [2, 3, -4, 5, 11, 6, 7]

print(sum_of_odds(0, li))
