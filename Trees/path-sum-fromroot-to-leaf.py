# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            targetSum -= root.val
            if targetSum ==0 and (root.left==None and root.right==None):
                return True
            if self.hasPathSum(root.left, targetSum):
                return True
            if self.hasPathSum(root.right, targetSum):
                return True
        return False
        