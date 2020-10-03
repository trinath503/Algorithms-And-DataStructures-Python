# class FloodFillAlgorithm:
#
#     def __init__(self):
#         self.description = 'Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.'
#         self.array = []
#         self.all_directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
#
#     def set_flod_fill(self, row_col_details, user_input_array_details):
#
#         if user_input_array_details is None:
#             # logger.info('Error hanlding at {} for reason {}'.format(time_details, error_message))
#             # retunr {'message': error_message}
#             print('Please enter a vlaid array')
#         else:
#             input_array = []
#             for each_row in range(row_col_details[0]):
#                 low_index = each_row * row_col_details[1]
#                 high_index = (each_row + 1) * row_col_details[1]
#                 input_array.append(user_input_array_details[low_index:high_index])
#
#             return input_array
#
#     def is_target_found(self, input_array, target_x, target_y, target_color):
#         return 0 <= target_x < len(input_array) and 0 <= target_y < len(input_array[0]) and input_array[target_x][
#             target_y] == target_color
#
#     def flod_fill_with_colour(self, input_array, target_x, target_y, replace_color):
#         q = []
#         q.append([target_x, target_y])
#         target_color = input_array[target_x][target_y]
#         while q:
#             x, y = q.pop(0)
#             input_array[x][y] = replace_color
#             for each_direction in self.all_directions:
#                 if self.is_target_found(input_array, x + each_direction[0], y + each_direction[1], target_color):
#                     q.append([x + each_direction[0], y + each_direction[1]])
#
#         return input_array
#
#     def genrate_results(self, input_array):
#         s = ''
#         for each_row in input_array:
#             for ele in each_row:
#                 s += str(ele) + ' '
#
#         s.rsplit(' ')
#         return s
#
#
# FFA = FloodFillAlgorithm()
# total_test_cases = int(input())
# for each_test in range(total_test_cases):
#     row_col_details = list(map(int, input().split(' ')))
#     user_input_array_details = list(map(int, input().split(' ')))
#     # print(row_col_details, user_input_array_details)
#     get_result = FFA.flod_fill_with_colour(input_array, target_x, target_y, replace_color)
#     input_array = FFA.set_flod_fill(row_col_details, user_input_array_details)
#     target_details = list(map(int, input().split(' ')))
#     target_x, target_y, replace_color = target_details
#     # print(target_x, target_y, replace_color)
#     # print(input_array)
#     print(FFA.genrate_results(get_result))

#
#
#
#

# from collections import deque


# Below lists details all 8 possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# check if it is possible to go to pixel (x, y) from
# current pixel. The function returns false if the pixel
# has different color or it is not a valid pixel
def isSafe(M, x, y, target):
	return 0 <= x < len(M) and 0 <= y < len(M[0]) and M[x][y] == target


# Flood fill using BFS
def floodfill(M, x, y, replacement):

	# create a queue and enqueue starting pixel
	q = []
	q.append((x, y))

	# get target color
	target = M[x][y]

	# loop till queue is empty
	while q:

		# pop front node from queue and process it
		x, y = q.pop(0)

		# replace current pixel color with that of replacement
		M[x][y] = replacement

		# process all 8 adjacent pixels of current pixel and
		# enqueue each valid pixel
		for k in range(len(row)):
			# if adjacent pixel at position (x + row[k], y + col[k]) is
			# a valid pixel and have same color as that of current pixel
			if isSafe(M, x + row[k], y + col[k], target):
				# enqueue adjacent pixel
				q.append((x + row[k], y + col[k]))


if __name__ == '__main__':

	# matrix showing portion of the screen having different colors
	M = [
			['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
			['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
			['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
			['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
			['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
			['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
			['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
			['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
			['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
			['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
	]

	# start node
	x = 3
	y = 9

	# target color = "X"
	# replacement color
	replacement = 'C'

	# replace target color with replacement color
	floodfill(M, x, y, replacement)

	# print the colors after replacement
	for r in M:
		print(r)

