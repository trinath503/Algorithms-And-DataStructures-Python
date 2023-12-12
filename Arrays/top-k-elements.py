class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        k_freq = {}

        for num in nums:

            if num not in k_freq:
                k_freq[num] = 1

            else:
                k_freq[num] += 1

        # sorted(k_freq.items(), key=lambda x: x, reverse=True)

        # return list(k_freq.keys())[:k]

        import heapq

        result = []
        for key, value in k_freq.items():
            heapq.heappush(result, (-value, key))

        return [heapq.heappop(result)[1] for _ in range(k)]