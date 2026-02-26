"""
HEAPS / PRIORITY QUEUES — Quick solution templates (this folder)
See: maximum-number-of-events-that-can-be-attended.py
"""

import heapq
from typing import List, Tuple

# (priority, item) — lower priority first in min-heap. For max-priority use -priority.


def max_events(events: List[List[int]]) -> int:
    events.sort(key=lambda x: x[0])
    heap = []  # min-heap of end days
    day = 1
    end_max = max(e[1] for e in events)
    i = 0
    attended = 0
    while day <= end_max:
        while i < len(events) and events[i][0] <= day:
            heapq.heappush(heap, events[i][1])
            i += 1
        while heap and heap[0] < day:
            heapq.heappop(heap)
        if heap:
            heapq.heappop(heap)
            attended += 1
        day += 1
    return attended


# Generic: push (priority, counter, task) to avoid comparing tasks; pop and use task.
