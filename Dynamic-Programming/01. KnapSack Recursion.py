def knapSack(weights, prices, capacity, current_index):
    # base case
    if current_index == 0 or capacity == 0: return 0

    # choice conditions
    if weights[current_index - 1] <= capacity:

        return  max(
            # include element
            prices[current_index-1]+knapSack(weights, prices, capacity - weights[current_index - 1], current_index - 1),
            # don't include element
            knapSack(weights, prices, capacity, current_index - 1)
        )

    elif weights[current_index - 1] > capacity:
        return knapSack(weights, prices, capacity, current_index - 1)


weights = [1, 3, 4, 5]
prices = [1, 4, 5, 7]
capacity = 10
print(knapSack(weights, prices, capacity, len(weights)))
