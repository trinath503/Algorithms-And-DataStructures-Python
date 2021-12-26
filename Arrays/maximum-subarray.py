# Using Kadane's Algorithm

import sys
class Solution:
    def maxSubArrayValue(self, nums: List[int]) -> int:
        
        # To store overall max value 
        global_max_sum = -sys.maxsize 
        
        # To store intermediate sub-array max value
        curr_sub_array_sum = -sys.maxsize

        # base case 
        if len(nums) <=1:
            return nums
        
        
        for each_num in nums:
            
            curr_sub_array_sum += each_num
            
            curr_sub_array_sum = max(curr_sub_array_sum , each_num)
            
            global_max_sum = max(global_max_sum, curr_sub_array_sum)
            
        return global_max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        
        # To store overall max value 
        global_max_sum = -sys.maxsize 
        
        # To store intermediate sub-array max value
        curr_sub_array_sum = -sys.maxsize

        # base case 
        if len(nums) <=1:
            return nums
        
        start = end = 0
        sub_array_start = 0

        for i in range(len(nums)):
            
            current_element = nums[i]
            curr_sub_array_sum += current_element
            
            if current_element > curr_sub_array_sum
                curr_sub_array_sum = current_element
                sub_array_start = i
            
            if curr_sub_array_sum > global_max_sum: 
                global_max_sum = curr_sub_array_sum
                start = sub_array_start
                end = i
            
        return nums[start: end+1]
            
            
            
        