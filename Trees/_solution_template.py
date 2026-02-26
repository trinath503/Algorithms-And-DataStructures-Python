"""
TREES (Binary Tree & BST) — Quick solution templates (FAANG quick reference)
Use this file to recall the pattern skeleton; see other .py files in this folder for full solutions.
"""

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# 1. DFS (RECURSIVE) — path, sum, exists, serialize
# When: "path sum", "max depth", "invert tree", "serialize"
# Time: O(n)  Space: O(h)
# =============================================================================
def dfs_path_sum(root: Optional[TreeNode], target: int) -> bool:
    if not root:
        return False
    target -= root.val
    if target == 0 and not root.left and not root.right:
        return True
    return dfs_path_sum(root.left, target) or dfs_path_sum(root.right, target)


def dfs_visit(root: Optional[TreeNode], result: List) -> None:
    if not root:
        return
    # Preorder: result.append(root.val)
    dfs_visit(root.left, result)
    # Inorder: result.append(root.val)
    dfs_visit(root.right, result)
    # Postorder: result.append(root.val)


# =============================================================================
# 2. BFS (LEVEL ORDER) — level-by-level, shortest path, min depth
# When: "level order", "min depth", "width", "serialize by level"
# Time: O(n)  Space: O(w)
# =============================================================================
def bfs_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result


# =============================================================================
# 3. FAST & SLOW / HEIGHT / DIAMETER
# When: "diameter", "balanced", "height", "middle"
# =============================================================================
def height(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root: Optional[TreeNode]) -> bool:
    def check(node):
        if not node:
            return 0
        L, R = check(node.left), check(node.right)
        if L == -1 or R == -1 or abs(L - R) > 1:
            return -1
        return 1 + max(L, R)
    return check(root) != -1


# =============================================================================
# 4. BST — INORDER (sorted), SEARCH, RANGE
# When: "BST", "kth smallest", "range sum", "validate BST"
# =============================================================================
def bst_search(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root or root.val == val:
        return root
    if val < root.val:
        return bst_search(root.left, val)
    return bst_search(root.right, val)


def bst_inorder_sorted(root: Optional[TreeNode], result: List[int]) -> None:
    if not root:
        return
    bst_inorder_sorted(root.left, result)
    result.append(root.val)
    bst_inorder_sorted(root.right, result)


# =============================================================================
# 5. BUILD TREE (from preorder/inorder or bracket string)
# When: "construct from preorder and inorder", "deserialize"
# =============================================================================
def build_from_pre_in(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    i = inorder.index(preorder[0])
    root.left = build_from_pre_in(preorder[1 : 1 + i], inorder[:i])
    root.right = build_from_pre_in(preorder[1 + i :], inorder[i + 1 :])
    return root
