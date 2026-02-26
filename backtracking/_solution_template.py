"""
BACKTRACKING — Quick solution templates (FAANG quick reference)
See: combination-sum, combination-sum-ii, permutations, subsets, N-Queens style.
"""

from typing import List

# =============================================================================
# TEMPLATE: collect all combinations/subsets that satisfy constraints
# 1. result = []
# 2. def backtrack(start_index, path, current_state):
# 3.   base: if goal met → result.append(path[:]); return
# 4.   prune: if invalid → return
# 5.   for i in range(start_index, n):
#        optional: skip duplicates (if i > start and arr[i]==arr[i-1]: continue)
#        path.append(arr[i])
#        backtrack(i or i+1, path, updated_state)  # i for reuse, i+1 for use once
#        path.pop()
# 6. backtrack(0, [], initial_state)
# 7. return result
# =============================================================================


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, path: List[int], total: int):
        if total > target:
            return
        if total == target:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])  # reuse same element
            path.pop()

    backtrack(0, [], 0)
    return result


def combination_sum_no_reuse(candidates: List[int], target: int) -> List[List[int]]:
    """Each element used at most once; sort and skip duplicates for unique combos."""
    candidates.sort()
    result = []

    def backtrack(start: int, path: List[int], total: int):
        if total > target:
            return
        if total == target:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start: int, path: List[int]):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def permutations(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(path: List[int], remaining: List[int]):
        if not remaining:
            result.append(path[:])
            return
        for i, x in enumerate(remaining):
            path.append(x)
            backtrack(path, remaining[:i] + remaining[i + 1 :])
            path.pop()

    backtrack([], nums)
    return result
