def knapSack(weights, prices, capacity, total_elements):
    # base case
    if total_elements == 0 or capacity == 0: return 0
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    for element in range(total_elements+1):
        for curr_capacity in range(capacity+1):

            if element ==0 or curr_capacity ==0:
                dp[element][curr_capacity] = 0
            elif weights[element - 1] <= curr_capacity:
                dp[element][curr_capacity] = max(
                    prices[element - 1]+dp[element-1][curr_capacity-weights[element-1]],
                    dp[element - 1][curr_capacity],
                )
            elif weights[element - 1] > curr_capacity:
                dp[element][curr_capacity] = dp[element - 1][curr_capacity]
    return dp[total_elements][capacity]


weights = [1, 3, 4, 5]
prices = [1, 4, 5, 7]
capacity = 10

print(knapSack(weights, prices, capacity, len(weights)))
