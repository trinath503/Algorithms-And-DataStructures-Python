# In-place rotate it by 90 degrees in clockwise direction
def rotate(mat):

	# Transpose the matrix
	for i in range(N):
		for j in range(i):
			temp = mat[i][j]
			mat[i][j] = mat[j][i]
			mat[j][i] = temp

	# swap columns
	for i in range(N):
		for j in range(N // 2):
			temp = mat[i][j]
			mat[i][j] = mat[i][N - j - 1]
			mat[i][N - j - 1] = temp

    '''
        if need to rotate in anti-close wise swap rows
    '''
    for i in range(N//2):
        for j in range(N // 2):
            temp = mat[i][j]
            mat[i][j] = mat[i][N - i - 1]
            mat[i][N - i - 1] = temp


if __name__ == '__main__':

	mat = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]
	]

	N = len(mat)

	rotate(mat)

	for i in range(N):
		print(mat[i])


