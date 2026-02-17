def findMaxItr(li: list) -> tuple:
    max_ele = li[0]
    idx = 0
    for i in range(1, len(li)):
        if li[i] > max_ele:
            max_ele = li[i]
            idx = i
    return (idx, max_ele)


def maxEle(li: list, idx: int) -> tuple:
    """
    return largest element and it's index
    """
    if idx >= len(li):
        return None, None
    # tup = maxEle(li, idx + 1)
    # cur_idx, cur_max = tup
    # or
    max_idx, cur_max = maxEle(li, idx + 1)
    if max_idx is None or li[idx] > cur_max:
        max_idx, cur_max = idx, li[idx]
    return max_idx, cur_max


def findMaxEle(li: list):
    return maxEle(li, 0)


numbers = [333, 2, 3, 4, 22, 5, 6, 7, 8, 10]

max = findMaxEle(numbers)
print(max)
