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

    def findMaximum(self, root):
        while root.right:
            root = root.right

        return  root

    # def findSuccessor(self,root, succ, key):
    #     #base case
    #     if root is None:
    #         return None
    #
    #     #check if key is equal to root value
    #     if root.data == key:
    #         if root.right:
    #             self.findMinimum(root.right)
    #
    #     #if value is less than right
    #     elif key < root.data:
    #         succ = root
    #         return  self.findSuccessor(root.left, succ, key)
    #
    #     else:
    #         return self.findSuccessor(root.right, succ, key)
    #
    #     return  succ

    def findPredecessor(self, root, predec, key):

        #root is empty
        if root is None:
            return None

        # root.value == key
        if root.data == key:
            if root.left:
                return self.findMaximum(root.left)

        # less
        elif key < root.data:
            return self.findPredecessor(root.left, predec, key)

        #greater
        else:
            predec = root
            return self.findPredecessor(root.right, predec, key)

        return predec



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

    keys = [15, 10, 20, 8, 12, 16, 25]
    binary_tree = BinaryTree()
    root = None
    for key in keys:
        root = binary_tree.insert_node(root, key)
    binary_tree.inodrer(root)
    succ = binary_tree.findPredecessor(root, None, 15)
    if succ:
        print('succ',succ.data)