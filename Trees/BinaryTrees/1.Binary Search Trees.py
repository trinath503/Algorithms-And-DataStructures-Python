class Tree:
    def __init__(self,data, left =None, right = None):
        self.left = left
        self.data = data
        self.right = right






class BinarySearchTree:

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


    def LevelOrder(self,root):
        # height = self.Height(root)\
        # print(root.data)
        if root is None:
            return 0
        # Create an empty queue for level order traversal
        levelOrderQueue = []
        # Enqueue Root and initialize height
        levelOrderQueue.append(root)
        while(len(levelOrderQueue)>0):
            # Print front of queue and remove it from queue
            print(levelOrderQueue[0].data)
            #Dequeue first element
            node = levelOrderQueue.pop(0)
            # Enqueue left child
            if node.left is not None:
                levelOrderQueue.append(node.left)
            if node.right is not None:
                levelOrderQueue.append(node.right)

    def Height(self,root):
        if root is None:
            return 0
        else:
            lheight = self.Height(root.left)
            rheight = self.Height(root.right)
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1
    def insert(self,root, node):
        if root is None:
            root = node
        else:
            if root.data < node.data:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                   self.insert(root.left, node)

    def minValueNode(node):
        current = node

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current



    def deletenode(self, root, key):
        print(root.data)
        # Base Case
        if root is None:
            return root

            # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if key < root.data:
            root.left = self.deletenode(root.left, key)

            # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif (key > root.data):
            root.right = self.deletenode(root.right, key)

            # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

                # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.data = temp.data
            # Delete the inorder successor
            root.right = self.deletenode(root.right, temp.data)

        return root




root =  Tree(50)
tri = BinarySearchTree()
node = Tree(30)
tri.insert(root, node)
node = Tree(20)
tri.insert(root, node)
node = Tree(40)
tri.insert(root, node)
node = Tree(70)
tri.insert(root, node)
node = Tree(60)
tri.insert(root, node)
node = Tree(80)
tri.insert(root, node)
node = Tree(90)
tri.insert(root, node)
print("PreOrder:")
tri.Preodrer(root)
print("Inorder:")
tri.inodrer(root)
print("PostOrder:")
tri.Postodrer(root)
tree_height = tri.Height(root)
print("Height is " ,tree_height)
print("LevelOrder:")
tri.LevelOrder(root)
