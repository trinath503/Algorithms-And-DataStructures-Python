# Dutch National Flag Problem, solved effectively using two pointers approach
# Time complexity is O(n) and space complexity is O(1)
# low points to the position where next o should be placed
# mid is used to iterate through array
# high points to the position where next 2 should be placed
def sortColors(colors):

    low = mid = 0
    high = len(colors)-1

    # base case
    if len(colors) == 1 or len(colors) ==0:
        return colors

    while mid <= high:

        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1

        elif colors[mid] == 1:
            mid +=1

        else:
            colors[mid], colors[high] = colors[high], colors[mid]
            high -=1

    return colors


colors = [2,0,2,1,1,0,2,1,0]
# colors = [1,0,1,1,1,0,1,1,0]
print(sortColors(colors))
