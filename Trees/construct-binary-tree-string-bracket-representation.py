class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None


def preOrder(node):
	if (node == None):
		return
	print(node.data, end=" ")
	preOrder(node.left)
	preOrder(node.right)


def treeFromStringHelper(si, ei, arr, root):

	if si[0] >= ei:
		return None

	if arr[si[0]] == "(":

		if arr[si[0]+1] != ")":
			if root.left is None:
				if si[0] >= ei:
					return
				new_root = newNode(arr[si[0]+1])
				root.left = new_root
				si[0] += 2
				treeFromStringHelper(si, ei, arr, new_root)

		else:
			si[0] += 2

		if root.right is None:
			if si[0] >= ei:
				return

			if arr[si[0]] != "(":
				si[0] += 1
				return

			new_root = newNode(arr[si[0]+1])
			root.right = new_root
			si[0] += 2
			treeFromStringHelper(si, ei, arr, new_root)
		else:
			return

	if arr[si[0]] == ")":
		if si[0] >= ei:
			return
		si[0] += 1
		return

	return


def treeFromString(string):

	root = newNode(string[0])

	if len(string) > 1:
		si = [1]
		ei = len(string)-1

		treeFromStringHelper(si, ei, string, root)

	return root

# Driver Code
if __name__ == '__main__':
	Str = "4(2(3)(1))(6(5))"
	root = treeFromString(Str)
	preOrder(root)

# This code is contributed by dheerajalimchandani
