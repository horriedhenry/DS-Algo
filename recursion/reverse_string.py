def rev_list(front: int, rear: int, li: list):
    # string are immutable in python so this does not work
    if front >= rear:
        return
    li[front], li[rear] = li[rear], li[front]
    rev_list(front + 1, rear - 1, li)


def rev_string(idx: int, s: str):
    # did it my self first try; don't know how.. but i got it
    if idx >= len(s):
        return ""

    # bottom-up
    # "" + e
    # e + r
    # er + i
    # eri + f
    # erif
    return rev_string(idx + 1, s) + s[idx]

    # fire := s[idx] + rev_string(idx + 1, s)
    # f + ire
    # i + re
    # r + e
    # e + ""
    # ""
    # return s[idx] + rev_string(idx + 1, s)


string = "fire"
string_rev = rev_string(0, string)
print(string_rev)
