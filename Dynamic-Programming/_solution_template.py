"""
DYNAMIC PROGRAMMING — Quick solution templates (FAANG quick reference)
See: climbing-stairs, house-robber, knapsack, subset-sum, coin-change, LIS, etc.
"""

from typing import List

# =============================================================================
# 1. LINEAR 1D DP (climbing stairs, house robber, min cost)
# Recurrence: f(i) from f(i-1), f(i-2)
# Time: O(n)  Space: O(n) or O(1) with variables
# =============================================================================
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, a + b
    return b


def house_robber(nums: List[int]) -> int:
    if not nums:
        return 0
    prev_no, prev_yes = 0, nums[0]
    for i in range(1, len(nums)):
        prev_no, prev_yes = max(prev_no, prev_yes), prev_no + nums[i]
    return max(prev_no, prev_yes)


# =============================================================================
# 2. KNAPSACK (0/1) — pick or skip each item
# dp[i][w] = max value using first i items and capacity w
# =============================================================================
def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


# =============================================================================
# 3. SUBSET SUM / EQUAL PARTITION
# dp[i][s] = can we form sum s using first i elements?
# =============================================================================
def subset_sum(nums: List[int], target: int) -> bool:
    dp = [True] + [False] * target
    for x in nums:
        for s in range(target, x - 1, -1):
            if dp[s - x]:
                dp[s] = True
    return dp[target]


# =============================================================================
# 4. UNBOUNDED (coin change ways, rod cutting)
# Same item can be used multiple times
# =============================================================================
def coin_change_ways(coins: List[int], amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]


# =============================================================================
# 5. LONGEST INCREASING SUBSEQUENCE (LIS)
# dp[i] = length of LIS ending at index i
# =============================================================================
def lis(nums: List[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# =============================================================================
# 6. 2D GRID DP (maximal square, unique paths)
# =============================================================================
def maximal_square(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    r, c = len(grid), len(grid[0])
    dp = [[0] * (c + 1) for _ in range(r + 1)]
    side = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i][j + 1], dp[i + 1][j])
                side = max(side, dp[i + 1][j + 1])
    return side * side
