"""
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
        # dp - Bottom up -> iterative + memoization
        # base case 
        if n ==0 : return 0
        
        if n == 1 : return 1
        
        dp = [ 0 for _ in range(n) ]
        
        dp[0] , dp[1] = 1, 2
        
        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
            
        return dp[-1] # return dp[n-1]
        
        """
        
        # using two vairables
        
        if n ==0 : return 0
        
        if n == 1 : return 1
        
        if n==2 : return 2
        
        first , second = 1, 2
        
        for i in range(2, n):
            current = first + second 
            
            first = second 
            second = current
        # print(first, second)
        return second 
        
    
        """
        # recursion 
        if n ==0 : return 0
        
        if n == 1 : return 1
        
        if n == 2: return 2
        
        return self.climbStairs(n-2)+ self.climbStairs(n-1)
        
        """
        