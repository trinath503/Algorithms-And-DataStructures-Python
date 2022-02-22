def knapSack(weights, prices, capacity, current_index, dp):
    # base case
    if current_index == 0 or capacity == 0: return 0

    if dp[current_index][capacity] != -1:
        return dp[current_index][capacity]
    # choice conditions
    if weights[current_index - 1] <= capacity:

        dp[current_index][capacity] = max(
            # include element
            prices[current_index-1]+knapSack(weights, prices, capacity - weights[current_index - 1], current_index - 1, dp),
            # don't include element
            knapSack(weights, prices, capacity, current_index - 1, dp)
        )
        return dp[current_index][capacity]

    elif weights[current_index - 1] > capacity:
        dp[current_index][capacity] = knapSack(weights, prices, capacity, current_index - 1, dp)
        return dp[current_index][capacity]


weights = [1, 3, 4, 5]
prices = [1, 4, 5, 7]
capacity = 10
dp = [[-1 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
print(knapSack(weights, prices, capacity, len(weights), dp))
