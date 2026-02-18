def maxEleRow(mat: list, r_idx: int, c_idx: int) -> tuple:
    """
    row major
    """
    if r_idx >= len(mat):
        return None, None
    elif c_idx >= len(mat[0]):
        return maxEle(mat, c_idx + 1, 0)

    max_row, max_col = maxEle(mat, r_idx, c_idx + 1)

    if max_row == None:
        max_row, max_col = r_idx, c_idx
    elif mat[r_idx][c_idx] > mat[max_row][max_col]:
        max_row, max_col = r_idx, c_idx

    return max_row, max_col


def maxEle(mat: list, r_idx: int, c_idx: int) -> tuple:
    """
    column major
    """
    if c_idx >= len(mat[0]):
        return None, None
    elif r_idx >= len(mat):
        return maxEle(mat, 0, c_idx + 1)

    max_row, max_col = maxEle(mat, r_idx + 1, c_idx)

    if max_row == None:
        max_row, max_col = r_idx, c_idx
    elif mat[r_idx][c_idx] > mat[max_row][max_col]:
        max_row, max_col = r_idx, c_idx

    return max_row, max_col


def findMaxMatrix(mat: list) -> tuple:
    return maxEle(mat, 0, 0)


mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

r, c = findMaxMatrix(mat)
print(mat[r][c])  # 12
