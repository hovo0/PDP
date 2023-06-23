"""
This module provides a binary search algorithm implementation.
"""


def binary_search(arr: list[int], target: int) -> int:
    """
    Search for target in a sorted array using binary search.

    :param arr: The sorted array.
    :param target: The target value to search for.
    :return: The index of the target value if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr: list[int] = [1, 3, 5, 7, 9]
target: int = 5

index = binary_search(arr, target)
print(index)  # 2

target: int = 9
index = binary_search(arr, target)
print(index)  # 4
