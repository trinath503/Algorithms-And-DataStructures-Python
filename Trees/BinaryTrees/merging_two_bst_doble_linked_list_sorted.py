# Data structure to store a BST node
class Node:
	# Constructor
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# Helper function to print a doubly linked list
def printDoublyList(head):

	while head:
		print(head.data, end=" -> ")
		head = head.right
	print("None")


# Function to insert a BST node at the front of a doubly linked list
def push(root, head):

	# insert the given node at the front of the DDL
	root.right = head

	# update the left pointer of the existing head node of the DDL
	# to point to the BST node
	if head:
		head.left = root

	# update the head pointer of DDL
	head = root
	return head


"""
Recursive function to convert a binary search tree into a doubly linked list
	root -. Pointer to the root node of the binary search tree
	head -. Reference to the head node of the doubly linked list
"""


def convertBSTtoDLL(root, head):

	# Base case
	if root is None:
		return head

	# recursively convert the right subtree a
	head = convertBSTtoDLL(root.right, head)

	# push current node at the front of the doubly linked list
	head = push(root, head)

	# recursively convert the left subtree
	head = convertBSTtoDLL(root.left, head)

	return head


# Recursive function to merge two doubly linked list into a
# single doubly linked list in sorted order
def mergeDDLs(a, b):

	# if the first list is empty, return the second list
	if a is None:
		return b

	# if the second list is empty, return the first list
	if b is None:
		return a

	# if head node of the first list is smaller
	if a.data < b.data:
		a.right = mergeDDLs(a.right, b)
		a.right.left = a
		return a

	# if head node of the second list is smaller
	else:
		b.right = mergeDDLs(a, b.right)
		b.right.left = b
		return b


# Function to merge two binary search trees into a doubly linked list
# in sorted order
def merge(a, b):

	# Convert first binary search tree to a doubly linked list
	first = convertBSTtoDLL(a, None)

	# Convert second binary search tree to a doubly linked list
	second = convertBSTtoDLL(b, None)

	# Merge both doubly linked lists
	return mergeDDLs(first, second)


if __name__ == '__main__':

	"""
	Construct first BST
		  20
		 /  \
		10 30
		   /  \
		  25 100
	"""

	a = Node(20)
	a.left = Node(10)
	a.right = Node(30)
	a.right.left = Node(25)
	a.right.right = Node(100)

	"""
	Construct second BST
		  50
		 /  \
		5   70
	"""

	b = Node(50)
	b.left = Node(5)
	b.right = Node(70)

	# merge both BSTs into a doubly linked list
	root = merge(a, b)
	printDoublyList(root)
