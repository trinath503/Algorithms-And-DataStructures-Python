class Solution:
    def tree2str(self, t: TreeNode) -> str:
        sb = [] # init string builder
        
        # helper function to create result
        def helper(node: TreeNode) -> None: 
            if not node:
                return
            
            sb.append(str(node.val))
            
            if not node.left and not node.right:
                # leaf node, stop processing
                return
            
            sb.append('(')          # always wrap left node with parenthesis when right node exist
            helper(node.left)       # process left node recursively 
            sb.append(')')                         

            if node.right:          # adding parenthesis for the right node only if it is not empty
                sb.append('(')
                helper(node.right)
                sb.append(')') 
        
        helper(t)

        return ''.join(sb)