def Element_Appears_Once():
    def __init():
        self.question_1 = 'Given an array of integers. All numbers occur twice except one number which occurs once. Find the number in O(n) time & constant extra space.'
        self.question_2 = 'Given an array where every element occurs three times, except one element which occurs only once. Find the element that occurs once.'

    def find_element_appears_array_every_element_appears_thrice(self, nums):
        #first solution - a
        return 3 * sum(set(nums)) - sum(nums)
        # first solution - b
        # for i in range(len(nums)):
        #     # print(nums[i], nums.count(nums[i]))
        #     if nums.count(nums[i]) == 1:
        #         return nums[i]

    def find_element_appears_array_every_element_appears_twice(self, nums):
        # second solution - a
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res
        # second solution - b
        #return 2 * sum(set(nums)) - sum(nums)


