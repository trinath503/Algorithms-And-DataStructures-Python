"""
HEAPS — Quick solution templates (FAANG quick reference)
See: MinHeap/, PriorityQueues/, top-k-elements (Arrays), merge-k-sorted (LinkedLists).
"""

import heapq
from typing import List

# Python heapq is a MIN-HEAP. For max-heap: push -x, pop -heapq.heappop(h).

# =============================================================================
# 1. TOP K LARGEST (min-heap of size k)
# Time: O(n log k)  Space: O(k)
# =============================================================================
def top_k_largest(nums: List[int], k: int) -> List[int]:
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap  # order may vary; for sorted: return sorted(heap, reverse=True)


# =============================================================================
# 2. TOP K FREQUENT (count freq, then heap of (freq, val) or quickselect)
# =============================================================================
def top_k_frequent(nums: List[int], k: int) -> List[int]:
    from collections import Counter
    count = Counter(nums)
    # min-heap of size k by frequency
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]


# =============================================================================
# 3. MERGE K SORTED LISTS (heap of (val, list_id, node_or_index))
# =============================================================================
def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    heap = []
    for i, arr in enumerate(lists):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    result = []
    while heap:
        val, list_id, idx = heapq.heappop(heap)
        result.append(val)
        if idx + 1 < len(lists[list_id]):
            heapq.heappush(heap, (lists[list_id][idx + 1], list_id, idx + 1))
    return result


# =============================================================================
# 4. KTH LARGEST IN STREAM (min-heap size k; top is kth largest)
# =============================================================================
def kth_largest_stream(stream: List[int], k: int) -> int:
    heap = stream[:k]
    heapq.heapify(heap)
    for x in stream[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]


# =============================================================================
# 5. INTERVAL / EVENTS (e.g. max events — sort by start, heap by end)
# =============================================================================
def max_events(events: List[List[int]]) -> int:
    """events[i] = [start, end]. Attend max number of events (one per day)."""
    events.sort(key=lambda x: x[0])
    end_max = max(e[1] for e in events)
    heap = []
    i = 0
    attended = 0
    for day in range(1, end_max + 1):
        while i < len(events) and events[i][0] <= day:
            heapq.heappush(heap, events[i][1])
            i += 1
        while heap and heap[0] < day:
            heapq.heappop(heap)
        if heap:
            heapq.heappop(heap)
            attended += 1
    return attended
