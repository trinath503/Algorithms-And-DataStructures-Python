"""
BITWISE — Quick solution templates (FAANG quick reference)
See: find-the-element-that-appears-once.py
"""

from typing import List

# =============================================================================
# 1. XOR — element that appears once (others twice)
# a ^ a = 0,  a ^ 0 = a,  XOR is commutative/associative
# Time: O(n)  Space: O(1)
# =============================================================================
def single_number_twice(nums: List[int]) -> int:
    res = 0
    for x in nums:
        res ^= x
    return res


# =============================================================================
# 2. EVERY ELEMENT THREE TIMES EXCEPT ONE
# Option A: 3 * sum(set(nums)) - sum(nums) (math)
# Option B: count bits mod 3 per position, reconstruct number
# =============================================================================
def single_number_thrice_math(nums: List[int]) -> int:
    return (3 * sum(set(nums)) - sum(nums)) // 2


def single_number_thrice_bits(nums: List[int]) -> int:
    ones = twos = 0
    for x in nums:
        twos |= ones & x
        ones ^= x
        threes = ones & twos
        ones &= ~threes
        twos &= ~threes
    return ones


# =============================================================================
# 3. USEFUL TRICKS
# =============================================================================
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def count_set_bits(n: int) -> int:
    c = 0
    while n:
        c += n & 1
        n >>= 1
    return c


def get_bit(n: int, i: int) -> int:
    return (n >> i) & 1


def set_bit(n: int, i: int) -> int:
    return n | (1 << i)
