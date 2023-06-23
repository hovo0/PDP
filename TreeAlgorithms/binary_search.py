def binary_search(arr, target):
    """
    Search for target in a sorted array using binary search.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 3, 5, 7, 9]
target = 5

index = binary_search(arr, target)
print(index)  # 2

target = 9
index = binary_search(arr, target)
print(index)  #4
