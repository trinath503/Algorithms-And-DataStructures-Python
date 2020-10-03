# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to check if given node is a leaf node or not
def isLeaf(node):
    return node.left is None and node.right is None


# Recursive function to find all nodes at given distance from leaf nodes
def leafNodeDistance(node, path, set, dist):

    # base case: empty tree
    if node is None:
        return

    # if a leaf node is found, insert the node at distance 'dist' from
    # leaf node into the set
    if isLeaf(node) and len(path) >= dist:
        set.add(path[-dist])
        return

    # include current node into current path
    path.append(node)

    # recur for left and right subtree
    leafNodeDistance(node.left, path, set, dist)
    leafNodeDistance(node.right, path, set, dist)

    # remove current node from the current path
    path.remove(node)


# find all distinct nodes at given distance from leaf nodes
def printLeafNodeDistance(node, dist):

    # list to store root to leaf path
    path = []

    # create an empty set to store distinct nodes at given
    # distance from leaf nodes
    s = set()

    # find all nodes
    leafNodeDistance(node, path, s, dist)

    # print output
    print([e.data for e in s])


if __name__ == '__main__':

    """ Construct below tree
               15
             /    \
            /      \
          10       20
         / \      /  \
        8   12   16  25
                /
               18
    """

    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    root.right.left.left = Node(18)

    dist = 1
    printLeafNodeDistance(root, dist)


