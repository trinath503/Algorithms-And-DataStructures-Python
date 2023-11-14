def merge_intervals(intervals):
    # base cases

    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x: x[0]) # sort based on the starting key
    result = [intervals[0]]

    # core logic
    for interval in intervals[1:]:

        if interval[0] < result[-1][1]:
            result[-1][1] = max(interval[1], result[-1][1])

        else:
            result.append(interval)

    return result


intervals = [[1, 3], [2, 6], [4, 7], [15, 18]]
print(merge_intervals(intervals))
