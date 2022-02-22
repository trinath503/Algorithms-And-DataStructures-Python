""""
This problem can be seen as follow-up question for problem 198. House Robber. Imagine, that we can already solve this problem: for more detailes please see my post:
https://leetcode.com/problems/house-robber/discuss/846004/Python-4-lines-easy-dp-solution-explained

Now, what we have here is circular pattern. Imagine, that we have 10 houses: a0, a1, a2, a3, ... a9: Then we have two possible options:

    Rob house a0, then we can not rob a0 or a9 and we have a2, a3, ..., a8 range to rob
    Do not rob house a0, then we have a1, a2, ... a9 range to rob.


"""

class Solution:
    def rob(self, houses: List[int]) -> int:
        total_houses = len(houses)
        
        if total_houses ==0 : return 0
            
        if total_houses == 1: return houses[0]

        if total_houses ==2: return max(houses[0], houses[1])
        
        def rob_helper(nums):
            
            n = len(nums)
            max_2_house_before ,max_1_house_before = 0 ,0 
            
            for i in range(n):
                current_house = max(nums[i] + max_2_house_before, max_1_house_before)
                max_2_house_before = max_1_house_before
                max_1_house_before = current_house
            # print(nums, max_2_house_before, max_1_house_before)
            return max(max_2_house_before, max_1_house_before)
        
        # print(houses[:total_houses-1],houses[1:])
        return max(
            houses[0]+rob_helper(houses[2:-1]),
            rob_helper(houses[1:])        
        )
                
                
        