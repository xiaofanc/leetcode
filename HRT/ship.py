"""
ships with different length on the grid
if hit . then return Missed
if hit a cell that was attacked before then return Already attacked
if hit the last cell of the ship then return Ship <x> sunk
if hit a cell that not the last cell then return Attacked ship <x>
"""

import collections
def solution(grid, shots):
    rows, cols = len(grid), len(grid[0])
    ships = collections.defaultdict(int)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ".":
                if grid[i][j] in ships:
                    ships[grid[i][j]] += 1
                else:
                    ships[grid[i][j]] = 1
    
    hitted = set()
    res = []
    for x, y in shots:
        if grid[x][y] == ".":
            res.append("Missed")
        else:
            if (x, y) in hitted:
                res.append("Already attacked")
            else:
                if ships[grid[x][y]] == 1:
                    s = "Ship " + str(grid[x][y])  + " sunk"
                else:
                    s = "Attacked ship " + str(grid[x][y])
                res.append(s)
                ships[grid[x][y]] -= 1
                hitted.add((x, y))
    return res
                
                    
                    
