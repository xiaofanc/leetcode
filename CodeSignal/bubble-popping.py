"""
pop bubble
click a bubble:
if the number of neighboring bubbles with same color >= 2: 
	- pop all bubbles
	- cell move move down to fill the gaps
fill empty cell with 0

bubbles = [
[3,2,4,4]
[3,1,2,1]
[1,1,1,4]
[3,1,2,2]
[3,3,3,4]
]

operations = [[2,1],[4,0],[3,2],[2,1]]

[2,1]:
[0,0,0,4]
[3,0,4,1]
[3,0,2,4]
[3,2,2,2]
[3,3,3,4]

[4，0]:
[0,0,0,4]
[0,0,4,1]
[0,0,2,4]
[3,0,2,2]
[3,2,3,4]

[3，2]:
[0,0,0,0]
[0,0,0,4]
[0,0,0,1]
[3,0,4,4]
[3,2,3,4]

[2，1]:
[0,0,0,0]
[0,0,0,4]
[0,0,0,1]
[3,0,4,4]
[3,2,3,4]
"""

def bubble_pop(bubbles, operations):
	m, n = len(bubbles), len(bubbles[0])
	dirs = [(0,1),(0,-1),(1,0),(-1,0)]
	
	for i, j in operations:
		cnt = 0                       # count neighbors with same color
		pops = [[] for _ in range(n)] # track rows to be poped for each column
		pops[j].append(i)
		for dx, dy in dirs:
			ni, nj = i+dx, j+dy
			if 0 <= ni < m and 0 <= nj < n and bubbles[ni][nj] == bubbles[i][j]:
				cnt += 1
				pops[nj].append(ni)
		if cnt >= 2:
			# pop bubbles for each column
			for c, rows in enumerate(pops):
				if rows:
					bottom, top, size = max(rows), min(rows), len(rows)
					# update from bottom until the first row
					for r in range(bottom,-1,-1):
						if r-size < 0:
							bubbles[r][c] = 0
						else:
							bubbles[r][c] = bubbles[r-size][c]

	return bubbles

bubbles = [[3,2,4,4],[3,1,2,1],[1,1,1,4],[3,1,2,2],[3,3,3,4]]
operations = [[2,1],[4,0],[3,2],[2,1]]
print(bubble_pop(bubbles, operations))

