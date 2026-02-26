"""
HASHING — Quick solution templates (FAANG quick reference)
Use for: two sum, count/frequency, anagrams, O(1) lookup. See also Arrays/two_sum, Strings/Anagrams.
"""

from typing import List
from collections import defaultdict, Counter

# =============================================================================
# 1. TWO SUM / COMPLEMENT LOOKUP
# =============================================================================
def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []


# =============================================================================
# 2. FREQUENCY / COUNT
# =============================================================================
def count_frequency(nums: List[int]) -> dict:
    return Counter(nums)


def group_by_key(items: List, key_fn) -> dict:
    groups = defaultdict(list)
    for x in items:
        groups[key_fn(x)].append(x)
    return dict(groups)


# =============================================================================
# 3. ANAGRAM (same chars, same count)
# =============================================================================
def is_anagram(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)


def anagram_key(s: str):
    """Key for grouping anagrams: sorted tuple or frozenset of (char, count)."""
    return tuple(sorted(s))


# =============================================================================
# 4. PREFIX SUM + HASH (subarray sum equals K)
# =============================================================================
def subarray_sum_count(nums: List[int], k: int) -> int:
    prefix = 0
    count = 0
    seen = defaultdict(int)
    seen[0] = 1
    for x in nums:
        prefix += x
        count += seen[prefix - k]
        seen[prefix] += 1
    return count


# =============================================================================
# 5. FIRST NON-REPEATING / FIRST UNIQUE
# =============================================================================
def first_unique_char(s: str) -> int:
    from collections import Counter
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1
