# # A linked list node
# class Node:
# 	def __init__(self, data=None, next=None):
# 		self.data = data
# 		self.next = next
#
#
# # Function to print given linked list
# def printList(head):
#
# 	ptr = head
# 	while ptr:
# 		print(ptr.data, end=" -> ")
# 		ptr = ptr.next
# 	print("None")
#
#
# # Function to sort linked list containing 0’s, 1’s and 2’s in single traversal
# def sortList(head):
#
# 	# base case
# 	if head is None or head.next is None:
# 		return head
#
# 	# maintain three dummy nodes
# 	zero_nodes = Node()
# 	one_nodes = Node()
# 	two_nodes = Node()
#
# 	# maintain three references
# 	zero = zero_nodes
# 	one = one_nodes
# 	two = two_nodes
#
# 	# traverse the list
# 	curr = head
# 	while curr:
# 		if curr.data == 0:
# 			zero.next = curr
# 			zero = curr
# 		elif curr.data == 1:
# 			one.next = curr
# 			one = curr
# 		else:
# 			two.next = curr
# 			two = curr
# 		curr = curr.next
#
# 	# combine lists containing 0's, 1's and 2's
# 	zero.next = one_nodes.next if one_nodes.next else two_nodes.next
# 	one.next = two_nodes.next
# 	two.next = None
#
# 	# change head and return
# 	return zero_nodes.next
#
#
# # Sort linked list containing 0’s, 1’s and 2’s in single traversal
# if __name__ == '__main__':
#
# 	# input keys
# 	keys = [1, 2, 0, 0, 1, 2, 1, 2, 1]
#
# 	head = None
# 	for i in reversed(range(len(keys))):
# 		print(i)
# 		head = Node(keys[i], head)
#
# 	head = sortList(head)
# 	printList(head)


# A linked list node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


# Function to print given linked list
def printList(head):
	ptr = head
	while ptr:
		print(ptr.data, end=" -> ")
		ptr = ptr.next
	print("None")


# Function to sort linked list containing 0’s, 1’s and 2’s in single traversal
def sortList(head):
	# head is present or not
	if head is None or head.next is None:
		return head
	# we need to create a reference -> dummy node
	zero_nodes = Node()
	zero = zero_nodes

	one_nodes = Node()
	one = one_nodes

	two_nodes = Node()
	two = two_nodes

	current_node = head
	while current_node:

		if current_node.data == 0:
			zero.next = current_node
			zero = current_node
		elif current_node.data == 1:
			one.next = current_node
			one = current_node
		else:
			two.next = current_node
			two = current_node

		current_node = current_node.next

	zero.next = one_nodes.next if one_nodes.next else two_nodes.next
	one.next = two_nodes.next
	two.next = None

	return zero_nodes.next


# Sort linked list containing 0’s, 1’s and 2’s in single traversal
if __name__ == '__main__':

	# input keys
	keys = [1, 2, 0, 0, 1, 2, 1, 2, 1]

	head = None
	for i in reversed(range(len(keys))):
		print(i)
		head = Node(keys[i], head)

	head = sortList(head)
	printList(head)
