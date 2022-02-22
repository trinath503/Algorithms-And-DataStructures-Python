class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
          dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        print(dp)
        return dp[-1] # return the last element
        
        
        """
        # solution -2 : use two variables and compute the max respectively
        n = len(nums)
        
        if n==0: return 0
        
        if n == 1: return nums[0]
        
        if n==2: max(nums[0], nums[1])
            
        
        first , second = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n):
            current = max(nums[i]+ first, second)
            
            first = second
            second =current 
            # print(first, second)
        return max(second, first)
        
        """

        
        