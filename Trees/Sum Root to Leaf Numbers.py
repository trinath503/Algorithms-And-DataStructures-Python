# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    def __init__(self):
        self.total = 0
        
    def findSum(self, root, val):
        if root==None:
            return 0
        
        val = (10*val)+ root.val
        # base case:
        if root.left  == None and root.right ==None :
            return val
        
        return self.findSum(root.left, val) + self.findSum(root.right,val)
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.findSum(root, 0)
        