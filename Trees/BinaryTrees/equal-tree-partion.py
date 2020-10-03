import collections

class Node:
    def __init__(self,data, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right


class BinaryTree:

    def Preodrer(self,root):
        if root:
            print(root.data)
            self.Preodrer(root.left)
            self.Preodrer(root.right)

    def inodrer(self,root):
        if root:
            self.inodrer(root.left)
            print(root.data)
            self.inodrer(root.right)

    def Postodrer(self,root):
        if root:
            self.Postodrer(root.left)
            self.Postodrer(root.right)
            print(root.data)

    def findMinimum(self, root):
        while root.left:
            root = root.left
        return root

    def getSumHelper(self,node, lookup):
        if not node:
            return 0
        total = node.data + \
                self.getSumHelper(node.left, lookup) + \
                self.getSumHelper(node.right, lookup)
        lookup[total] += 1
        return total

    def count(self,root):
        if root == None:
            return 0
        return self.count(root.left) + self.count(root.right) + 1

    def checkEqualTree(self, root, n):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False

        if( self.count(root) == n - self.count(root) ):
            return True

        return self.checkEqualTree(root.left, n) or self.checkEqualTree(root.right, n)

    def check(self,root):

        total = self.count(root)

        return  self.checkEqualTree(root, total)


    def insert_node(self,root,data):
        node = Node(data)
        if root is None:
            root = node
        else:
            if root.data > node.data:
                root.left = self.insert_node(root.left, data)
            else:
                root.right = self.insert_node(root.right, data)
        return root


if __name__ == '__main__':

    ''' Construct below BST
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
    '''

    # keys = [15, 10, 20, 8, 12, 16, 25]
    keys = [5,1,6,3,7,4]
    binary_tree = BinaryTree()
    root = None
    for key in keys:
        root = binary_tree.insert_node(root, key)
    binary_tree.inodrer(root)
    succ = binary_tree.check(root)
    print(succ)