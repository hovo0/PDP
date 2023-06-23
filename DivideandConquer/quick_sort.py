"""
This module provides an implementation of the quicksort algorithm.
"""


def quick_sort(arr):
    """
    Sorts the given array using the quicksort algorithm.

    :param arr: The array to be sorted.
    :return: The sorted array.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left_arr, right_arr, middle_arr = [], [], []

    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num > pivot:
            right_arr.append(num)
        else:
            middle_arr.append(num)

    return quick_sort(left_arr) + middle_arr + quick_sort(right_arr)


arr = [3, 1, 15, 45, 4853, 4, 45, 45, 453, 46878, 46, 1, 5, 4, 3, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # [1, 1, 3, 3, 4, 4, 5, 5, 15, 45, 45, 45, 46, 453, 4853, 46878]
