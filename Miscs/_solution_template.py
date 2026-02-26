"""
MISCS — Quick solution templates (FAANG quick reference)
See: LRU Cache.py, Next-closest-time.py, solid-principles.py
"""

from typing import Optional
from collections import OrderedDict

# =============================================================================
# 1. LRU CACHE (OrderedDict or dict + doubly linked list)
# get: move to end (most recent); put: add at end, evict from front if over capacity
# =============================================================================
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # mark as recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


# =============================================================================
# 2. RANDOM / TIME-BASED (next closest time: try all combinations, pick valid)
# =============================================================================
def next_closest_time_idea(time: str) -> str:
    """Given HH:MM, return next time using only digits from time (smallest next)."""
    # Parse digits; generate all valid HH:MM; pick smallest > current in circular order.
    pass  # see Next-closest-time.py for full solution


# =============================================================================
# 3. DESIGN PATTERNS (reference only — see solid-principles.py)
# =============================================================================
# Single responsibility, Open/closed, Liskov, Interface segregation, Dependency inversion.
