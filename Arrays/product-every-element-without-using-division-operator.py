# Function to replace each element of the list with product
# of every other element without using division operator
def findProduct(A):

    n = len(A)

    # use two auxiliary lists
    left = [None] * n
    right = [None] * n

    # left[i] stores the product of all elements in the sublist[0..i-1]
    left[0] = 1
    for i in range(1, n):
        left[i] = A[i - 1] * left[i - 1]
    print(left)
    # right[i] stores the product of all elements in sublist[i+1..n-1]
    right[n - 1] = 1
    for j in reversed(range(n - 1)):
        right[j] = A[j + 1] * right[j + 1]
    print(right)
    # replace each element with product of its left and right sublist
    for i in range(n):
        A[i] = left[i] * right[i]


if __name__ == '__main__':

    # A = [5, 3, 4, 2, 6, 8]
    A = [2,3,4,5]
    findProduct(A)

    # print the modified list
    print(A)
