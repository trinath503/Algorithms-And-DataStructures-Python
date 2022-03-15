# Python program to find minimum time required
# to burn the binary tree completely
 
# Definition for a  binary tree node
 
 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
 # Using BFS , we need to do for every level
 
class Solution:
    # Class Variable
    res = 0
 
    def levelOrder(self, root, nodes_map, target):
        if root is None:
            return None
        target_node = None
        level_queue = []
        level_queue.append(root)
        level_count =1
        while len(level_queue):
            # print("level no {}".format(level_count))
            current_queue_width = len(level_queue)
            while current_queue_width:
                #first element in queue
                current_node = level_queue.pop(0)
                if target == current_node.val:
                    target_node = current_node
                    
                # print(current_node.val)
                if current_node.left:
                    nodes_map[current_node.left.val]= current_node
                    level_queue.append(current_node.left)
                if current_node.right:
                    nodes_map[current_node.right.val]= current_node
                    level_queue.append(current_node.right)
                #current queue decrement
                current_queue_width -=1

            # level increment
            level_count +=1

        return nodes_map, target_node

    def calcTime(self, root, res, nodes_map):
        target_node = None
        level_queue = []
        level_queue.append(root)
        level_count =1
        visited_nodes = set()
        while len(level_queue):
            # print("level no {}".format(level_count))
            current_queue_width = len(level_queue)
            flag = 0
            while current_queue_width:
                #first element in queue
                current_node = level_queue.pop(0)
                
                    
                # print(current_node.val)
                if current_node.left and current_node.left.val not in visited_nodes:
                    flag = 1
                    visited_nodes.add(current_node.left.val)
                    level_queue.append(current_node.left)
                if current_node.right and current_node.right.val not in visited_nodes:
                    flag = 1
                    visited_nodes.add(current_node.right.val)
                    level_queue.append(current_node.right)
                parent_node = nodes_map[current_node.val] if current_node.val in nodes_map else None
                if parent_node and parent_node.val not in visited_nodes:
                    flag = 1
                    visited_nodes.add(parent_node.val)
                    level_queue.append(parent_node)
                #current queue decrement
                current_queue_width -=1
            # print(level_count, level_queue, res)
            # level increment
            if flag:
                res += 1
            level_count +=1

        return res

    # Driver function to calculate minimum
    # time required
    def solve(self, root, target):
        nodes_map = {}
        target_node = None
        self.res = 0
        nodes_map, target_node = self.levelOrder(root, nodes_map, target)
        # print(nodes_map, target_node)
        if target_node:
            self.res = self.calcTime(target_node, self.res, nodes_map)
        return self.res
 
 
# Driver Code
if __name__ == '__main__':
    # Construct tree shown in the above example
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.left.left.left = TreeNode(8)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(10)
    root.left.right.left.left = TreeNode(11)
 
    # Target Leaf Node
    target = 11
 
    # Print min time to burn the complete tree
    s = Solution()
    print(s.solve(root, target))