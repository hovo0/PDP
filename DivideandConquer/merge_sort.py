"""
This module provides an implementation of the merge sort algorithm.
"""


def merge_sort(array):
    """
    Sorts the given array using the merge sort algorithm.

    :param array: The array to be sorted.
    :return: The sorted array.
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_arr = array[:mid]
    right_arr = array[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.

    :param left_arr: The left sorted array.
    :param right_arr: The right sorted array.
    :return: The merged and sorted array.
    """
    result = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    result += left_arr[i:]
    result += right_arr[j:]

    return result


array = [3, 1, 4, 1, 456, 454, 15, 2, 512, 455412, 1515, 4415, 47, 521, 0]
sorted_arr = merge_sort(array)
print(sorted_arr)  # [0, 1, 1, 2, 3, 4, 15, 47, 454, 456, 512, 521, 1515, 4415, 455412]
