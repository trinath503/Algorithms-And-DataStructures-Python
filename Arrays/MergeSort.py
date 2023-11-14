
def merge_sort(arr):

    length = len(arr)

    if length <= 1:
        return arr

    mid = length // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_half = merge_sort(left_arr)
    right_half = merge_sort(right_arr)

    return merge(left_half, right_half)


def merge(left, right):

    merged = []

    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1


    # append if anything left over
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged




arr = [2 ,5 ,6 ,3 ,65, 23 ,7 ,91 ,4]
print(merge_sort(arr))
