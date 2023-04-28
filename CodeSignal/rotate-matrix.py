"""
You are given a nxn two-dimensional square matrix and an integer turns. Your task is to rotate
the matrix "over diagonals" turns times and return the final matrix. The process of rotation:
The elements on the two main diagonals stay the same after rotation, but the four segments
divided by these diagonals are rotated to change places in a clockwise direction.
It is guaranteed that the matrix size is an odd number.

matrix:
[[1, 2, 3, 4,5]
 [6, 7, 8, 9,10]
 [11,12,13,14,15]
 [16,17,18,19,20]
 [21,22,23,24,25]]

after rotation 1 time:
[[1, 16,11, 6,5]
 [22,7, 12, 9,2]
 [23,18,13, 8,3]
 [24,17,14,19,4]
 [21,20,15,10,25]]

matrix:
[[1,2,3]
 [4,5,6]
 [7,8,9]]

after rotation 1 time:
[[1,4,3]
 [8,5,2]
 [7,6,9]]

matrix:
[[1,2,1]
 [5,1,3]
 [1,4,1]]

after rotation 2 times:
[[1,5,1]
 [4,1,2]
 [1,3,1]]

[[1,4,1]
 [3,1,5]
 [1,2,1]]

"""

def rotate_matrix_turns(matrix, turns):
	def helper(matrix):
		l, r = 0, len(matrix)-1
		while l < r:
			top, bottom = l, r
			for i in range(1, r-l):
				topLeft = matrix[top][l+i]
				matrix[top][l+i] = matrix[bottom-i][l]
				matrix[bottom-i][l] = matrix[bottom][r-i]
				matrix[bottom][r-i] = matrix[top+i][r]
				matrix[top+i][r] = topLeft
			l += 1
			r -= 1
		return matrix
	for i in range(turns % 4):
		matrix = helper(matrix)
	return matrix

matrix = [[1, 2, 3, 4,5],[6, 7, 8, 9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
turns = 1
print(rotate_matrix_turns(matrix, turns))

matrix = [[1,2,1],[5,1,3],[1,4,1]]
turns = 2
print(rotate_matrix_turns(matrix, turns))





