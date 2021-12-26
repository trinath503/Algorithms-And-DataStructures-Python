# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# import sys 
# class Solution:
#     def __init__(self): 
#         self.maxSum = -sys.maxsize
        
#     def findMax(self, root):
#         # default case 
#         if root == None:
#             return 0
        
#         left = self.findMax(root.left)
#         right = self.findMax(root.right)
        
#        self.maxSum = max(left + right + root.val, self.maxSum)
        
#         result = root.val + max(left,right)
#         if result < 0:
#             return 0
#         else:
#             return result
    
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         self.findMax(root)
#         return self.maxSum
        
        
        















import sys
 
 
# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 









# Recursive function to find the maximum sum path between two leaves
# in a binary tree
def findMaxSumPath(root, max_sum=-sys.maxsize):
 
    # base case: when node is empty
    if root == None:
        return 0, max_sum

    left, max_sum = findMaxSumPath(root.left, max_sum)

    right, max_sum = findMaxSumPath(root.right, max_sum)

    # case 1: when left node is empty 
    if root.left == None:
        return (right +root.data), max_sum

    # case 2: when right node is empty
    if root.left == None:
        return (left +root.data), max_sum

    cur_sum = left + right + root.data

    max_sum = max(max_sum, cur_sum)

    # case 3: when both left & right nodes present 
    return  (max(left, right) + root.data), max_sum
 
if __name__ == '__main__':
 
    ''' Construct the following tree
          1
        /   \
       /     \
      2       3
       \     / \
       -4   5   6
           / \
          7   8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(-4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    print(findMaxSumPath(root)[1])