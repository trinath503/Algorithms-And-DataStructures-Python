"""
GRAPHS — Quick solution templates (FAANG quick reference)
See: BFS - Recursion.py, DFS - Recursion.py, evaluate-division, GraphCreation, etc.
"""

from typing import List, Dict
from collections import deque, defaultdict

# =============================================================================
# 1. GRAPH REPRESENTATION (adjacency list)
# =============================================================================
def build_undirected(edges: List[List[int]], n: int) -> Dict[int, List[int]]:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return dict(graph)


def build_directed(edges: List[List[int]]) -> Dict[int, List[int]]:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return dict(graph)


# =============================================================================
# 2. BFS (shortest path in unweighted, level order)
# =============================================================================
def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> int:
    if start == end:
        return 0
    q = deque([start])
    visited = {start}
    steps = 0
    while q:
        steps += 1
        for _ in range(len(q)):
            u = q.popleft()
            for v in graph.get(u, []):
                if v == end:
                    return steps
                if v not in visited:
                    visited.add(v)
                    q.append(v)
    return -1


def bfs_traversal(graph: Dict[int, List[int]], start: int) -> List[int]:
    order = []
    q = deque([start])
    visited = {start}
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order


# =============================================================================
# 3. DFS (recursive — path, cycle, topological sort)
# =============================================================================
def dfs_recursive(graph: Dict[int, List[int]], start: int, visited: set) -> List[int]:
    order = []
    def dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
    dfs(start)
    return order


def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    stack = [start]
    visited = set()
    order = []
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                stack.append(v)
    return order


# =============================================================================
# 4. GRID (4/8 directions, islands)
# =============================================================================
DIRS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs_grid(grid: List[List[str]], r: int, c: int, visited: set) -> None:
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or (r, c) in visited:
        return
    visited.add((r, c))
    for dr, dc in DIRS_4:
        dfs_grid(grid, r + dr, c + dc, visited)


# =============================================================================
# 5. TOPOLOGICAL SORT (Kahn's or DFS post-order)
# =============================================================================
def topological_sort_kahn(graph: Dict[int, List[int]], n: int) -> List[int]:
    indeg = [0] * n
    for u in graph:
        for v in graph[u]:
            indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []  # empty if cycle
