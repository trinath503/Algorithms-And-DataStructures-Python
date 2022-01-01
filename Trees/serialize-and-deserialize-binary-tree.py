# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        if not root: 
            return 'x'
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        q = deque()
        q.extend(data.split(","))
        self.data = q
        root = self.deserialize_helper()
        return root
        
    def deserialize_helper(self):
        if self.data[0] == 'x':
            self.data.popleft()
            return None
        node = TreeNode(self.data.popleft()) 
        node.left = self.deserialize_helper()
        node.right = self.deserialize_helper()
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



# Solution -2
# class Codec:
#     def serialize(self, root):
#         # take care of base cases
#         # if a node is empty, add 'x' to string
#         # you can set 'x' to any mark as you want
#         if not root: return 'x'
#         # preoder(Root->left->right)
#         # ex,
#         #     1
#         #    / \
#         #   2   3
#         #      / \
#         #     4   5 
#         # 
#         # return (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
#         # if you look at the return statement very closely, it is actually very intuitive
#         # for value 1, you have 2 as left child and 3 as right child
#         # for value 2, you have 'x'(None) as left child and 'x'(None) as right child which indicates it is a leaf node
#         return root.val, self.serialize(root.left), self.serialize(root.right)

#     def deserialize(self, data):
#         #######################INTUITION#########################
#         # The initial data string will be something like below:
#         # (1, (2, 'x', 'x'), (3, (4, 'x', 'x'), (5, 'x', 'x')))
#         # if you loop through string: 
#         # 1                                 -> this is node value
#         # (2, 'x', 'x')                     -> this is node left
#         # (3, (4, 'x', 'x'), (5, 'x', 'x')) -> this is node right
#         ########################################################
#         # always take care of base case: if the node's value is 'x' then return None
#         if data[0] == 'x': return None
#         # create new treenode for node value
#         node = TreeNode(data[0])
#         # do the recursive to unpack string value
#         node.left = self.deserialize(data[1])
#         node.right = self.deserialize(data[2])
#         # return the new TreeNode that we just created
#         return node