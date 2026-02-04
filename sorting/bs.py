# for every iteration the larget element will be at the end

def bubble_sort(arr):
    size = len(arr)

    for i in range(1, size):
        for j in range(size - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_v2(arr):
    size = len(arr)

    for i in range(size):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_while(arr):
    size = len(arr)
    i = 0
    while i < size:
        j = 0
        while j < size - 1 - i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1

arr = [i for i in range(10, 0, -1)]
bubble_while(arr)
print(arr)
