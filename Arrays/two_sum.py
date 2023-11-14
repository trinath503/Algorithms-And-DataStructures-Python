class FindTwoSum:
    def __int__(self):
        self.descrption = 'we need to find the indexs of the given arra'

    def find_indexes(self, given_array, target):
        store_ele_indexs = dict()
        for indx, ele in enumerate(given_array):
            current_difference = target - ele

            print(store_ele_indexs,current_difference, given_array)
            if current_difference in store_ele_indexs:
                return [store_ele_indexs[current_difference], indx]

            store_ele_indexs[ele] = indx

        return  []


t = FindTwoSum()
arr = [1,3,5,6,4]
target = 7

print(t.find_indexes(arr, target))


# Solution -2: if the array is sorted , time complexity is O(n) even though sorted array is O(nlogn), space complexity is O(1)

def two_sum_sorted(nums, target):

    left, right = 0, len(nums)-1

    while left < right:

        current_sum = nums[left]+nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

    
