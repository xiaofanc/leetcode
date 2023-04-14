"""
draw 5 types of figures on the n x m grid.
5 figures:
A:[[1]]
B:[[1,1,1]]
C:
[[1,1]
 [1,1]]
D:
[[1,0]
 [1,1]
 [1,0]]
E:
[[0,1,0]
 [1,1,1]]

create a matrix of integers representing the grid paper and draw the figures based on rules:
- start with all 0
- place the figures on the grid in the order they appear in figures, do not overlap
- of all the available locations, choose the lowest row index
- if there are multiple possible locations with the lowest row index, choose the lowest column index
- it's guaranteed that all figures will fit on the grid
- return the grid

n = 4
m = 4
figures = ['D','B','A','C']
res:
[[1,2,2,2]
 [1,1,3,0]
 [1,4,4,0]
 [0,4,4,0]]

n = 3
m = 5
figures = ['A','D','E'] 
res:
[[1,2,0,0,0]
 [0,2,2,3,0]
 [0,2,3,3,3]]
"""

def draw_figures(n, m, figures):
	grid = [[0 for j in range(m)] for i in range(n)]
	mappings = {'A':[(0,0)], 'B':[(0,0),(0,1),(0,2)], 'C':[(0,0),(0,1),(1,0),(1,1)], 'D':[(0,0),(1,0),(2,0),(1,1)], 'E':[(0,0),(1,-1),(1,0),(1,1)]}

	for idx, f in enumerate(figures):
		lst = mappings[f]
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 0:
					# check all cells needed
					draw = True
					for dx, dy in lst:
						if not (0 <= i+dx < n and 0 <= j+dy < m and grid[i+dx][j+dy] == 0):
							draw = False
					if draw:
						for dx, dy in lst:
							grid[i+dx][j+dy] = idx+1
				else:
					draw = False
					continue
				if draw:
					break # j
			if draw:
				break # i
	return grid

n = 4
m = 4
figures = ['D','B','A','C']
print(draw_figures(n, m, figures))

n = 3
m = 5
figures = ['A','D','E'] 
print(draw_figures(n, m, figures))





