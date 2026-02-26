"""
BINARY SEARCH TREE (BST) — Quick solution templates (this subfolder)
Use for: BST operations, kth smallest, range queries, merge two BSTs.
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# BST SEARCH / INSERT
# =============================================================================
def bst_search(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root or root.val == val:
        return root
    return bst_search(root.left, val) if val < root.val else bst_search(root.right, val)


def bst_insert(root: Optional[TreeNode], val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root


# =============================================================================
# INORDER → SORTED LIST (kth smallest: collect inorder and take [k-1])
# =============================================================================
def bst_to_sorted_list(root: Optional[TreeNode]) -> List[int]:
    out = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        out.append(node.val)
        inorder(node.right)
    inorder(root)
    return out


# =============================================================================
# RANGE SUM / RANGE QUERY (inorder prune)
# =============================================================================
def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0
    if root.val < low:
        return range_sum_bst(root.right, low, high)
    if root.val > high:
        return range_sum_bst(root.left, low, high)
    return root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)


# =============================================================================
# MERGE TWO BSTs (inorder both → merge sorted lists → build balanced BST or return list)
# =============================================================================
def merge_two_sorted_lists(a: List[int], b: List[int]) -> List[int]:
    i, j = 0, 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:] or b[j:])
    return out
