# here we go.. forgot this for a moment
# C++'s equivalent is pretty simple...

# arr = [1]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def binary_search_hi_exclusive(arr, key):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid
    return -1

def binary_search(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


key = 2
# found = binary_search(arr, key)
found = binary_search_hi_exclusive(arr, key)

if found != -1:
    print(f"element {key} found at idx {found}")
else:
    print("not found")
