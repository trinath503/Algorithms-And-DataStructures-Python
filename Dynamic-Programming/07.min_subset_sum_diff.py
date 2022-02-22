def subSetSumProblem(weights, total_sum, total_elements):
    # base case
    if total_elements == 0 or total_sum == 0: return 0
    dp = [[0 if j != 0 else 1 for j in range(total_sum + 1)] for _ in range(len(weights) + 1)]
    # print(dp)
    for element in range(1,total_elements + 1):
        for curr_sum in range(1,total_sum + 1):
            if weights[element - 1] <= curr_sum:
                dp[element][curr_sum] = dp[element - 1][curr_sum - weights[element - 1]] + dp[element - 1][curr_sum]
            else:
                dp[element][curr_sum] = dp[element - 1][curr_sum]
    # print(dp)
    possible_sums = []

    for i in range(total_sum+1):
        if dp[total_elements][i]:
            possible_sums.append(i)

    return possible_sums


# weights = [2,3,5,6,8,10]
weights = [1,2,7]
capacity = sum(weights)
possible_sums = subSetSumProblem(weights, capacity, len(weights))
print(possible_sums)
min_diff = capacity
for ele in possible_sums:
    min_diff = min(min_diff, abs(capacity - 2*ele))

print(f' min difference can be  formed is {min_diff}')

