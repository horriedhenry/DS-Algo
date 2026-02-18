def maxEleM(li: list, left: int, right: int) -> int:
    """
    My solution := return idx
    """
    if left == right:
        return left

    mid = (left + right) // 2
    l_max = maxEleM(li, 0, mid)
    r_max = maxEleM(li, mid + 1, right)

    if li[l_max] > li[r_max]:
        return l_max
    return r_max


def maxEleB(li: list, left: int, right: int) -> int:
    """
    Another approach := return the max element itself (Better)
    """
    if left == right:
        return li[left]

    # just use the max function
    mid = (left + right) // 2
    # l_max = maxEleB(li, 0, mid)
    # r_max = maxEleB(li, mid + 1, right)
    # max_ele = max(l_max, r_max)
    # return max_ele
    # or simply :-
    return max(maxEleB(li, 0, mid), maxEleB(li, mid + 1, right))


def findMaxEle(li):
    _len = len(li)
    if _len == 0:
        return None
    return maxEleB(li, 0, _len - 1)


li = [5, 2, -5, -4, 30, 3, 200, 7, 5, 20]

max_ele = findMaxEle(li)
print(max_ele)  # 200
