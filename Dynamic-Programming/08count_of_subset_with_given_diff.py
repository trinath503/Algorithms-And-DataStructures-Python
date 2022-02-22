def subSetSumCountProblem(weights, total_sum, total_elements):
    # base case
    if total_elements == 0 or total_sum == 0: return 0
    dp = [[0 if j != 0 else 1 for j in range(total_sum + 1)] for _ in range(len(weights) + 1)]

    for element in range(1,total_elements + 1):
        for curr_sum in range(1,total_sum + 1):
            if weights[element - 1] <= curr_sum:
                dp[element][curr_sum] = dp[element - 1][curr_sum - weights[element - 1]] + dp[element - 1][curr_sum]
            else:
                dp[element][curr_sum] = dp[element - 1][curr_sum]

    return dp[total_elements][total_sum]

#
# weights = [2,3,5,6,8,10]
# diff = 2


weights = [1,1,2,3]
diff = 1
capacity = (sum(weights)+ diff)//2

# sum1 - sum2 = diff -> eq_1
# sum1 + sum2 = total_sum
# sum1 = (diff+ total_sum)/2
# if sum1 -> sub_set_1 number of possible count is equal to sub_set_2 count -> where diff matches
if capacity %2 !=0:
    print(" Zero subsets found")
else:
    print(subSetSumCountProblem(weights, capacity, len(weights)))
