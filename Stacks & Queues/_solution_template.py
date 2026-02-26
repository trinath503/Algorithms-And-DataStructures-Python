"""
STACKS & QUEUES — Quick solution templates (FAANG quick reference)
See: rotting-apples-or-oranges.py (BFS with queue); valid parentheses (stack) in Strings.
"""

from typing import List
from collections import deque

# =============================================================================
# 1. STACK (list or collections.deque)
# Use: parentheses, next greater element, monotonic stack, DFS iterative
# =============================================================================
def stack_demo():
    stack = []
    stack.append(1)
    stack.append(2)
    top = stack.pop()   # 2
    peek = stack[-1]    # 1


def valid_parentheses_stack(s: str) -> bool:
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
# 2. QUEUE (collections.deque for BFS, level order)
# =============================================================================
def queue_bfs_demo(graph: dict, start: int) -> list:
    q = deque([start])
    visited = {start}
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order


# =============================================================================
# 3. MULTI-SOURCE BFS (e.g. rotting oranges — all rotten cells as initial queue)
# =============================================================================
def multi_source_bfs_grid(grid: List[List[int]]) -> int:
    """Grid: 0 empty, 1 fresh, 2 rotten. Return minutes to rot all, or -1."""
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    if fresh == 0:
        return 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    minutes = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
        if fresh == 0:
            return minutes
    return -1


# =============================================================================
# 4. MONOTONIC STACK (next greater element, histogram area)
# =============================================================================
def next_greater_element(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # indices
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
