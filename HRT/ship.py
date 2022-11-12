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
                
                    
                    
