def subSetSumProblem(weights, total_sum, total_elements):
    # base case
    if total_elements == 0 or total_sum == 0: return 0
    dp = [[False if j != 0 else True for j in range(total_sum + 1)] for _ in range(len(weights) + 1)]
    for element in range(1,total_elements + 1):
        for curr_sum in range(1,total_sum + 1):
            if weights[element - 1] <= curr_sum:
                dp[element][curr_sum] = dp[element - 1][curr_sum - weights[element - 1]] or dp[element - 1][curr_sum]
            elif weights[element - 1] > curr_sum:
                dp[element][curr_sum] = dp[element - 1][curr_sum]
    return dp[total_elements][total_sum]


def equalSumPartitionProblem(weights, total_elements):
    total_sum = sum(weights)

    # // if sum is odd --> not possible to make equal partitions
    if total_sum % 2 != 0: return False

    sub_sum = total_sum//2
    print(sub_sum)
    return subSetSumProblem(weights, sub_sum, total_elements)


weights = [1, 2, 4, 5] # true  -> {1,5} , {2,4}
# weights = [1, 3, 4, 5] # false

print(equalSumPartitionProblem(weights, len(weights)))
