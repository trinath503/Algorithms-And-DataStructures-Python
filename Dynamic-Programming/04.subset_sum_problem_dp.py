def subSetSumProblem(weights, total_sum, total_elements):
    # base case
    if total_elements == 0 or total_sum == 0: return 0
    dp = [[False if j!=0 else True for j in range(total_sum+1) ] for _ in range(len(weights)+1)]
    for element in range(1, total_elements+1):
        for curr_sum in range(1, total_sum+1):
            if weights[element - 1] <= curr_sum:
                dp[element][curr_sum] = dp[element-1][curr_sum-weights[element-1]] or dp[element - 1][curr_sum]
            elif weights[element - 1] > curr_sum:
                dp[element][curr_sum] = dp[element - 1][curr_sum]
    return dp[total_elements][total_sum]


weights = [1, 3, 4, 5]
total_sum = 133

print(subSetSumProblem(weights, total_sum, len(weights)))
