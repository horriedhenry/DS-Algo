# Find the minimum element in the unsorted array and swap it with the element in the beginning


def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                # loop for min index from i + 1 to end
                min_idx = j

        # if first ele in unsorted part is > min_ele swap
        # [1, 4, 2, 3, 5] we assume min_idx = i, and there's no min_ele in [4, 2, 3, 5]
        # so it swaps with it self
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# li = [i for i in range(10, 0, -1)]
li = [1, 4, 2, 3, 5]
selection_sort(li)
print(li)
