"""
There are a row ofnhouses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by anx3cost matrix. For example,costs[0][0]is the cost of painting house 0 with color red;costs[1][2]is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

"""

class PaintHouse:


    def findMinCostToPaint(self, houses):

        if not houses or len(houses) ==0: return 0

        dp = [[0 for i in range(3)] for i in range(len(houses))]

        for i in range(1, len(houses)):

            dp[i][0] = houses[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = houses[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = houses[i][2] + min(dp[i-1][1], dp[i-1][0])

            # without using dp 
            # cost -> houses 
            # costs[i][0] += Math.min(costs[i - 1][1], costs[i - 1][2]);
            # costs[i][1] += Math.min(costs[i - 1][0], costs[i - 1][2]);
            # costs[i][2] += Math.min(costs[i - 1][0], costs[i - 1][1]);

        
        res = min(dp[-1][0], dp[-1][1])
        res = min(res, dp[-1][2])
        return res