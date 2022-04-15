def binary_search(arr, low, high, target_element):

    

    while low <= high:

        mid = (low+high)//2

        if arr[mid] == target_element:
            return mid

        elif arr[mid] > target_element:
            high = mid -1

        elif arr[mid] < target_element:
            low = mid +1

    return -1

arr = [1,2,3,4]
print(binary_search(arr, 0, len(arr),3 ))
print(binary_search(arr, 0, len(arr)-1,31 ))