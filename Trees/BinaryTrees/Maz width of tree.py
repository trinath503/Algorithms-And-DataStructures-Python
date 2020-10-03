
# Data structure to store a Binary Tree node
class Node:
	def __init__(self, key=None, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right


# Function to find maximum width of the tree using level order
# traversal of given binary tree
def maxWidth(root):

	# return if tree is empty
	if root is None:
		return

	# create an empty queue and enqueue root node
	queue = []
	queue.append(root)

	# stores maximum width
	max = 0
	level =0

	# loop till queue is empty
	while queue:
		level +=1
		if level%2==0:
			print("Dont swapp level:", level)
		# calculate number of nodes in current level
		# This is equal to width of current level
		width = len(queue)

		# update maximum width if number of nodes in current level
		# is more than maximum width found so far
		if max < width:
			max = width

		# process every node of current level and enqueue their
		# non-empty left and right child to queue
		while width > 0:
			width = width - 1
			curr = queue.pop(0)

			if curr.left:
				queue.append(curr.left)

			if curr.right:
				queue.append(curr.right)

	print("Maximum width is", max)


if __name__ == '__main__':

	root = Node(15)
	root.left = Node(10)
	root.right = Node(20)
	root.left.left = Node(8)
	root.left.right = Node(12)
	root.right.left = Node(16)
	root.right.right = Node(25)

	maxWidth(root)
