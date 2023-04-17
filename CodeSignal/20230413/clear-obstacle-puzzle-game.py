"""
If you are playing a gravity-based puzzle game that involve clearing obstacles to allow an irregularly-shaped figure to fall to the bottom.
You are given a rectangular matrix board representing the game board, which only contains:
'.' - empty cell
'#' - obstacle
'*' - figure

It is guaranteed that the figure consists of one piece, where all parts are connected by the sides.
Your task is to simulate how the figure should fall and find the minimum number of obstacles that should be removed 
to let the figure finally touch the bottom of the board with at least one of its cells.

board = [['*','*','*'],['#','*','*'],['*','*','.'],['.','.','.'],['.','#','#']]
res = 2
"""

def clear_obstacles_puzzle(board):
	m, n = len(board), len(board[0])

	# get the least step to reach to bottom for the figure
	step = m
	for i in range(m-1,-1,-1):
		for j in range(n):
			if board[i][j] == '*':
				step = m-1-i
				break # j
		if step < m:
			break # i

	# if already touch the bottom or no obstacles
	if step == 0 or step == m:
		return 0

	# move figure step by step and calculate the obstacles on the way
	cols = [[] for i in range(n)]
	for i in range(m):
		for j in range(n):
			if board[i][j] == '*':
				cols[j].append(i)
	res = 0
	for j, col in enumerate(cols):
		if col: # there is part of figure in column j
			top, bottom = min(col), max(col)
			for i in range(top, bottom+step+1):
				if board[i][j] == '#':
					res += 1
	return res


board = [['*','*','*'],['#','*','*'],['*','*','.'],['.','.','.'],['.','#','#']]
print(clear_obstacles_puzzle(board))

board = [['*','*','*'],['*','.','*'],['*','.','*'],['.','#','.'],['.','#','.']]
print(clear_obstacles_puzzle(board))






