"""
- start from left
- compare element on the right with elements on left part
- where left part is sorted and right part is not
- inserting elements in correct position in the sorted array.

it's like a shuffled deck of cards you compare a card with other cards and place it in correct position.
"""


def insertion_sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i + 1, size):
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1


li = [i for i in range(10, 0, -1)]
insertion_sort(li)
print(li)
