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
    def isLeaf(self,node):
        return node.left is None and node.right is None
    def leafNodeDistance(self, node, store_paths, store_nodes, min_distance_from_leaf):
        print(node.data, store_paths, store_nodes)
        #if root is None
        if node is None:
            return

        #
        if self.isLeaf(node) and len(store_paths) >= min_distance_from_leaf:
            store_nodes.add(store_paths[-min_distance_from_leaf])
            return

        store_paths.append(node)
        self.leafNodeDistance(node.left, store_paths, store_nodes, min_distance_from_leaf)
        self.leafNodeDistance(node.right, store_paths, store_nodes, min_distance_from_leaf)

        store_paths.remove(node)

    def findMinimumPath(self, root, min_distance_from_leaf):

        store_paths = []
        store_nodes = set()

        self.leafNodeDistance(root, store_paths, store_nodes, min_distance_from_leaf)
        for ele in store_nodes:
            print(ele.data)
        # print(store_nodes)


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
    binary_tree.findMinimumPath(root, 1)
