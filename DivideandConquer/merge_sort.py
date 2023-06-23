def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
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
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5,4,7,9,456,454,15,2,512,455412,1515,4415,47,521,0]
sorted_arr = merge_sort(arr)
print(sorted_arr) # [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 9, 9, 15, 47, 454, 456, 512, 521, 1515, 4415, 455412]
