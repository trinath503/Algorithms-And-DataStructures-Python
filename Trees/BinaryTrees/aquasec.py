
#         15
#       /.  \
#       /     \
#      10.     20
#             /. \
#           17   23
#          /. \  22, 25
#         16.  18



class Node:
    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right



class PrintRightNodes:
    # def __init__
    def insert_node(self, root ,node):

        if root == None:
            root = node
        if root.data > node.data:
            root.left = self.insert_node(root.left, node)
        if root.data < node.data:
            root.right = self.insert_node(root.right, node)
        return root

    def traversal(self,root):
        if root ==None:
            return
        self.traversal(root.left)
        print(root.data)
        self.traversal(root.right)


    def print_right_tree_nodes(self, root, isRoot=False):
        # print(root)
        if root is None:
            return None
        if isRoot and root:
            print(root.data)
        if root.right is not None:
            print(root.right.data)
            self.print_right_tree_nodes(root.right)
        if root.left is not None:
            if root.left.right is not None:
                print(root.left.right.data)
                self.print_right_tree_nodes(root.left.right)


array_elements = [15, 10, 20, 17, 23, 16, 18, 22, 25]
root = None
print_object = PrintRightNodes()
for ele in array_elements:
    node = Node(ele)
    root = print_object.insert_node(root, node)
print_object.traversal(root)
print('-'*50)
print_object.print_right_tree_nodes(root, True)

# 10
# / \
#     8
# 12
# /  \ / \
#     4
# 9
# 11
# 14
#
# Vertical
# line - 1: 4
# Vertical
# line - 2: 8
# Vertical
# line - 3: 10 + 9 + 11 = 30
# Vertical
# line - 4: 12
# Vertical
# line - 5: 14

[1,2,3,4,5,6,7,8]

sorted(given_array, )
