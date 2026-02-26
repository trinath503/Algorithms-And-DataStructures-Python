"""
MATRIX / 2D GRID — Quick solution templates (FAANG quick reference)
See: NumberOfIslands.py, FloodFill.py; also Arrays/number-of-islands.py
"""

from typing import List
from collections import deque

# =============================================================================
# 1. DIRECTIONS (4 or 8)
# =============================================================================
DIRS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRS_8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


# =============================================================================
# 2. DFS ON GRID (flood fill, count islands)
# =============================================================================
def dfs_grid(grid: List[List[str]], r: int, c: int, visited: set) -> None:
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if grid[r][c] == "0" or (r, c) in visited:
        return
    visited.add((r, c))
    for dr, dc in DIRS_4:
        dfs_grid(grid, r + dr, c + dc, visited)


def num_islands_dfs(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and (i, j) not in visited:
                dfs_grid(grid, i, j, visited)
                count += 1
    return count


# =============================================================================
# 3. BFS ON GRID (shortest path, multi-source e.g. rotting oranges)
# =============================================================================
def bfs_grid_levels(grid: List[List[int]], starts: List[tuple]) -> int:
    """starts = list of (r, c); return minutes to cover all reachable."""
    rows, cols = len(grid), len(grid[0])
    q = deque(starts)
    visited = set(starts)
    steps = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in DIRS_4:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if grid[nr][nc] == 1:  # fresh
                        visited.add((nr, nc))
                        q.append((nr, nc))
        if q:
            steps += 1
    return steps


# =============================================================================
# 4. FLOOD FILL (replace color at (sr, sc) and all connected same color)
# =============================================================================
def flood_fill(grid: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    old = grid[sr][sc]
    if old == new_color:
        return grid
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != old:
            return
        grid[r][c] = new_color
        for dr, dc in DIRS_4:
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return grid
