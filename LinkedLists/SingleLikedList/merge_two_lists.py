# A linked list node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


# Helper function to print given linked list
def printList(msg, head):

	print(msg, end='')
	ptr = head
	while ptr:
		print(ptr.data, end=" -> ")
		ptr = ptr.next
	print("None")



# Takes two lists sorted in increasing order, and merge their nodes
# together to make one big sorted list which is returned
def SortedMerge(l1, l2):


    curr = dummy = Node()
    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next





if __name__ == '__main__':

	a = b = None
	for i in reversed(range(1, 8, 2)):
		a = Node(i, a)

	for i in reversed(range(2, 7, 2)):
		b = Node(i, b)

	# print both linked list
	printList("First List  : ", a)
	printList("Second List : ", b)

	head = SortedMerge(a, b)
	printList("After Merge : ", head)
