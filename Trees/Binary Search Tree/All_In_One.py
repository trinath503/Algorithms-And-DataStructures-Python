'''
    class for creating new node
        @params data: value to assign for creating node
        #rtype: None
'''
class Node:
    # function initialization
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.data = data
        self.right = right


class BinarySearchTree:

    def __init__(self, description=None):
        self.description = 'description'


    def add_node(self, root, element: int)-> None:

        if isinstance(element, int):

            if root is None:
                node = Node(element)
                root = node

            elif root.data > element:
                root.left = self.add_node(root.left, element)

            else:
                root.right = self.add_node(root.right, element)

            return root
        else:
            return {'status': 'Error', 'message': 'Input data is not valid, please give integer values for adding new nodes'}



    '''
        Returns the pre-order of the current tree
        @params root: starting node of the tree
        @rtype: None
    '''
    def preOrder(self, root ):
        if root == None:
            return None
        else:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)



    '''
        Returns the inorder of the current tree
        @params root: starting node of the tree
        @rtype: None
    '''
    def inOrder(self, root ):
        if root == None:
            return None
        else:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)


    '''
        Returns the post-order of the current tree
        @params root: starting node of the tree
        @rtype: None
    '''
    def postOrder(self, root ):
        if root == None:
            return None
        else:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)


    '''
        Returns the levelOrder  of the current tree
        @params root: starting node of the tree
        @rtype: None
    '''
    def levelOrder(self,root):
        if root is None:
            return None

        level_queue = []
        level_queue.append(root)
        level_count =1
        while len(level_queue):
            print("level no {}".format(level_count))
            current_queue_width = len(level_queue)
            while current_queue_width:
                #first element in queue
                current_node = level_queue.pop(0)
                print(current_node.data)
                if current_node.left:
                    level_queue.append(current_node.left)
                if current_node.right:
                    level_queue.append(current_node.right)
                #current queue decrement
                current_queue_width -=1

            # level increment
            level_count +=1

    '''
        Returns the levelOrder  of the current tree
        @params root: starting node of the tree
        @rtype: None
    '''
    def AdjacentLevelOrder(self,root):
        if root is None:
            return None

        level_queue = []
        level_queue.append(root)
        level_count =1
        while len(level_queue):
            print("level no {}".format(level_count))
            current_queue_width = len(level_queue)
            while current_queue_width:
                #first element in queue
                current_node = level_queue.pop(0)
                if level_count%2:
                    print(current_node.data)
                if current_node.left:
                    level_queue.append(current_node.left)
                if current_node.right:
                    level_queue.append(current_node.right)
                #current queue decrement
                current_queue_width -=1

            # level increment
            level_count +=1

    def leftViewOfTree(self,root):
        if root is None:
            return None
        else:
            tree_queue = []
            tree_queue.append(root)
            while len(tree_queue):
                currenlt_level = len(tree_queue)
                current_node = tree_queue.pop(0)
                first_element = True
                while currenlt_level:
                    if first_element:
                        print(current_node.data)
                        first_element = False

                    if current_node.left:
                        tree_queue.append(current_node.left)
                    if current_node.right:
                        tree_queue.append(current_node.right)

                    currenlt_level -=1

    def BottomView(self,root, level , distance, bottomViewMap):
        #following pre-order of tree
        if root is None:
            return None

        #
        if distance not in bottomViewMap:
            bottomViewMap[distance] = {'level': level, 'data': root.data}
        else:
            if level >=bottomViewMap[distance]['level'] :
                bottomViewMap[distance] = {'level': level, 'data': root.data}

        self.BottomView(root.left, level+1, distance-1, bottomViewMap)
        self.BottomView(root.right, level+1, distance+1, bottomViewMap)

        return bottomViewMap

    def BottomViewOfTree(self, root):
        if root is None:
            return root
        level = 1
        distance  = 0
        bottomViewMap ={}
        bottomViewElements = self.BottomView(root, level, distance, bottomViewMap)
        for ele in sorted(bottomViewElements.items(), key= lambda item: item[0]):
            print(ele[1]['data'])




    def TopViewTree(self, root, level=1, distance=0, map_details={}):
        if root is None:
            return

        if distance not in map_details:
            map_details[distance] = root.data

        self.TopViewTree(root.left, level+1, distance-1, map_details)
        self.TopViewTree(root.right, level+1, distance+1, map_details)

        return map_details


    def RightView(self, root, level=1, lastLevel=0, map_details={}):
        if root is None:
            return lastLevel

        if level > lastLevel:
            map_details[level] = root.data
            lastLevel = level

        lastLevel = self.RightView(root.right , level+1, lastLevel, map_details)
        lastLevel = self.RightView(root.left , level+1, lastLevel, map_details)



    def diagonalViewNegativeSlope(self, root, level=1, map_details= {}):
        if root is None:
            return
        else:

            if level not in map_details:
                map_details[level] = [root.data]
            else:
                map_details[level].append(root.data)

            self.diagonalViewNegativeSlope(root.left, level+1, map_details)
            self.diagonalViewNegativeSlope(root.right, level, map_details)

        return map_details

    def SpiralOrderView(self, root, level=1, spiral_flow='left', map_details=[]):

        if root is None:
            return
        else:

            q = []
            q.append(root)
            level = False
            while len(q):
                current_level_length = len(q)
                while current_level_length:

                    if level:
                        current_node = q.pop(0)
                        map_details.append(current_node.data)
                        if current_node.left:
                            q.append(current_node.left)
                        if current_node.right:
                            q.append(current_node.right)
                    else:
                        current_node = q.pop()
                        map_details.append(current_node.data)
                        if current_node.right:
                            q.insert(0, current_node.right)
                        if current_node.left:
                            q.insert(0, current_node.left)

                    current_level_length -= 1
                level = not level

        return map_details






if __name__=='__main__':
    total_elements = int(input())
    root = None
    t = BinarySearchTree()
    for ele in range(total_elements):
        root = t.add_node(root, int(input()))

#     # pre-order of tree
#     print('pre-order view of tree')
#     t.preOrder(root)

#     # pre-order of tree
#     print('inorder view of tree')
#     t.inOrder(root)

#     # pre-order of tree
#     print('postorder view of tree')
#     t.postOrder(root)

    #level order of tree
    print('level order of tree ')
    t.levelOrder(root)

#     #level order of tree
#     print('Adjacent level order')
#     t.AdjacentLevelOrder(root)

    #left view of tree
    print('left view of tree')
    t.leftViewOfTree(root)





