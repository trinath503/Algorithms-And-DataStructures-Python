"""
ARRAYS — Quick solution templates (FAANG quick reference)
Use this file to recall the pattern skeleton; see other .py files in this folder for full solutions.
"""

from typing import List, Optional
from collections import deque

# =============================================================================
# 1. TWO POINTERS (sorted array, pairs, palindrome)
# When: "two numbers that sum to X", "remove duplicates", "valid palindrome"
# Time: O(n)  Space: O(1)
# =============================================================================
def two_pointers_sorted(nums: List[int], target: int) -> Optional[List[int]]:
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return None


# =============================================================================
# 2. SLIDING WINDOW (subarray/substring, contiguous, at most K)
# When: "longest substring with K distinct", "max sum of size K", "minimum window"
# Time: O(n)  Space: O(k) or O(1)
# =============================================================================
def sliding_window_fixed_k(nums: List[int], k: int) -> List[int]:
    """Max in each window of size k — use deque to keep indices of useful elements."""
    q = deque()
    result = []
    for i in range(len(nums)):
        if q and i - q[0] >= k:
            q.popleft()
        while q and nums[q[-1]] < nums[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            result.append(nums[q[0]])
    return result


def sliding_window_variable(s: str) -> int:
    """e.g. longest substring with at most K distinct — expand/shrink with dict."""
    window = {}
    low = high = 0
    best = 0
    while high < len(s):
        # add s[high], update window
        window[s[high]] = window.get(s[high], 0) + 1
        while len(window) > 2:  # or your condition
            window[s[low]] -= 1
            if window[s[low]] == 0:
                del window[s[low]]
            low += 1
        best = max(best, high - low + 1)
        high += 1
    return best


# =============================================================================
# 3. BINARY SEARCH (sorted array OR binary search on answer)
# When: "sorted array", "find in O(log n)", "min capacity", "Kth smallest"
# Time: O(log n)  Space: O(1)
# =============================================================================
def binary_search(arr: List[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# =============================================================================
# 4. HASH MAP (two sum, count, frequency)
# When: "two sum", "count occurrences", "find in O(1)"
# Time: O(n)  Space: O(n)
# =============================================================================
def two_sum_hash(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []


# =============================================================================
# 5. KADANE / MAX SUBARRAY (contiguous sum)
# When: "maximum subarray sum", "largest sum contiguous"
# Time: O(n)  Space: O(1)
# =============================================================================
def max_subarray_kadane(nums: List[int]) -> int:
    best = curr = nums[0]
    for i in range(1, len(nums)):
        curr = max(nums[i], curr + nums[i])
        best = max(best, curr)
    return best


# =============================================================================
# 6. PREFIX / RUNNING STATE (range queries, running sum)
# When: "subarray sum equals K", "running sum", "prefix"
# =============================================================================
def prefix_count_subarray_sum(nums: List[int], k: int) -> int:
    from collections import defaultdict
    prefix_sum = 0
    count = 0
    seen = defaultdict(int)
    seen[0] = 1
    for x in nums:
        prefix_sum += x
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] += 1
    return count
