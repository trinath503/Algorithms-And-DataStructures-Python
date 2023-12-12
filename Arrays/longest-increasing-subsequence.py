class Solution:

    # solution  O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:


        tails = [1] * len(nums)


        for i in range(1, len(nums)):

            for j in range(0, i):


                if nums[i] > nums[j] and tails[i] < tails[j] +1:

                    tails[i] = tails[j] + 1



        return max(tails)

    # solution O(nlogn)
    n = len(nums)
    tails = [0] * n

    size = 0

    for num in nums:

        i, j = 0, size

        while i!=j:

            mid = (i+j) //2

            if tails[i] < num :
                i += 1

            else:
                j = mid

        tails[i] = num

        size = max(i+1, size)

