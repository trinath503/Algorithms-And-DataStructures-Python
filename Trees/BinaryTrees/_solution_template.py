"""
TREES / BINARY TREES — Quick solution templates (this subfolder)
Use for: symmetric tree, invert, width, inorder successor/predecessor, nodes at distance.
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# SYMMETRIC / MIRROR
# =============================================================================
def is_symmetric(root: Optional[TreeNode]) -> bool:
    def mirror(l, r):
        if not l and not r:
            return True
        if not l or not r or l.val != r.val:
            return False
        return mirror(l.left, r.right) and mirror(l.right, r.left)
    return mirror(root, root) if root else True


# =============================================================================
# INVERT TREE
# =============================================================================
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# =============================================================================
# MAX WIDTH (level order with index)
# =============================================================================
def max_width(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    q = deque([(root, 0)])
    best = 0
    while q:
        n = len(q)
        left = q[0][1]
        for _ in range(n):
            node, idx = q.popleft()
            if node.left:
                q.append((node.left, 2 * idx))
            if node.right:
                q.append((node.right, 2 * idx + 1))
        best = max(best, (idx - left + 1) if q or n else 1)
    return best


# =============================================================================
# INORDER SUCCESSOR (BST: leftmost of right subtree, or first parent going up)
# =============================================================================
def inorder_successor_bst(root: Optional[TreeNode], p: TreeNode) -> Optional[TreeNode]:
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ


# =============================================================================
# NODES AT DISTANCE K FROM LEAF (DFS, track path, mark at distance k)
# =============================================================================
def nodes_at_k_from_leaf(root: Optional[TreeNode], k: int) -> List[int]:
    result = []
    path = []
    seen = set()

    def dfs(node):
        if not node:
            return
        path.append(node)
        if not node.left and not node.right:
            if len(path) > k and id(path[-1 - k]) not in seen:
                seen.add(id(path[-1 - k]))
                result.append(path[-1 - k].val)
        dfs(node.left)
        dfs(node.right)
        path.pop()

    dfs(root)
    return result
