""" 
Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]

"""
# sort, nest loop, two pointer approach - O(n^2) ,O(1)
def threeUniqueTriplets(nums, target):
    nums.sort()
    result = []

    for i in range(len(nums) -2):

        if i >0 and nums[i] == nums[i-1]:
            continue # skip duplicates

        left , right = i+1, len(nums)-1

        while left < right:

            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1 # skip duplicates
                while left < right and nums[right] == nums[right-1]:
                    right -= 1 # skip duplicates

                left +=1
                right -= 1

            elif current_sum < target:
                left +=1
            else:
                right -=1

        return result

nums = [1,0,-1, 0,-2, 2,3,4]
target = 0 # target = 2
print(threeUniqueTriplets(nums, target))

# solution -2 
def sum_of_tripltes():

def Unique_Triplets():
    all_triplets = []
    for i in given_array:
        first_ele = [i]
        rest_elements = []
        for j in given_array:
            if i==j:
                continue
            rest_elements.append(j)
            if len(rest_elements)==2:
                cur_triplet = first_ele+rest_elements
                if sum(cur_triplet) ==0:
                    all_triplets.append(cur_triplet)



# quadrapules

def quaduplets(nums, target):

    nums.sort()
    result = []

    for i in range(len(nums)-3):

        if i >0 and nums[i] == nums[i-1]:
            continue # skip duplicates

        for j in range(i+1, len(nums)-2):

            if j > i+1 and nums[j] == nums[j-1]:
                continue # skip duplicates

            left, right = j+1, len(nums)-1

            while left < right:

                curent_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if curent_sum == target:
                    result.append([nums[i] , nums[j] , nums[left] , nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1  # skip duplicates

                    while left < right and nums[right] == nums[right-1]:
                        right -=1   # skip duplicates

                    left += 1
                    right -=1

                elif curent_sum < target:
                    left +=1

                else:
                    right -=1

    return result







nums = [1,0,-1, 0,-2, 2,3,4]
target = 1
print(quaduplets(nums, target))
