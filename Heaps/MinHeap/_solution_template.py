"""
HEAPS / MIN HEAP — Quick solution templates (this folder)
See: maximum-number-of-events-that-can-be-attended.py
"""

import heapq
from typing import List

# Min-heap: smallest element at top. heapq.heappush(h, x), heapq.heappop(h), heapq.heapify(list)


def top_k_smallest(nums: List[int], k: int) -> List[int]:
    heapq.heapify(nums)
    return heapq.nsmallest(k, nums)


def max_events_attend(events: List[List[int]]) -> int:
    """Sort by start day; for each day add available events (by end day) to min-heap; pop one."""
    events.sort(key=lambda x: x[0])
    max_day = max(e[1] for e in events)
    heap = []
    i = 0
    count = 0
    for day in range(1, max_day + 1):
        while i < len(events) and events[i][0] <= day:
            heapq.heappush(heap, events[i][1])
            i += 1
        while heap and heap[0] < day:
            heapq.heappop(heap)
        if heap:
            heapq.heappop(heap)
            count += 1
    return count
