"""
STRINGS — Quick solution templates (FAANG quick reference)
See: valid-palindrome, longest-palindromic-substring, Anagrams, encode-decode-tinyurl, etc.
"""

from typing import List
from collections import defaultdict, Counter


# =============================================================================
# 1. TWO POINTERS — palindrome check, reverse
# =============================================================================
def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


# =============================================================================
# 2. EXPAND AROUND CENTER — longest palindromic substring
# Time: O(n^2)  Space: O(1)
# =============================================================================
def expand(s: str, lo: int, hi: int) -> str:
    while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
        lo -= 1
        hi += 1
    return s[lo + 1:hi]


def longest_palindrome(s: str) -> str:
    best = ""
    for i in range(len(s)):
        odd = expand(s, i, i)
        even = expand(s, i, i + 1)
        best = max(best, odd, even, key=len)
    return best


# =============================================================================
# 3. ANAGRAM — sort or counter
# =============================================================================
def is_anagram(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # or frozenset(Counter(s).items())
        groups[key].append(s)
    return list(groups.values())


# =============================================================================
# 4. VALID PARENTHESES — stack
# =============================================================================
def valid_parentheses(s: str) -> bool:
    stack = []
    pair = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in pair:
            if not stack or stack[-1] != pair[c]:
                return False
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0


# =============================================================================
# 5. SLIDING WINDOW — longest substring with K distinct / no repeat
# =============================================================================
def longest_substring_k_distinct(s: str, k: int) -> int:
    window = {}
    left = best = 0
    for right, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        while len(window) > k:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
