"""
if the robot does not hit the boarder or hits "1":
    continue move
    if the new cell is clean:
        mark as visited
        res += 1
else:
    change directions
if (r, c, state) is in visited: # stop condition
    return res
add (r, c, state) in visited
"""

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = 1
        col, row = len(room[0]), len(room)
        state = r = c = 0
        visited = set()
        room[0][0] = -1
        
        while True:
            dx, dy = directions[state][0], directions[state][1]
            newr, newc = r+dx, c+dy
            if 0 <= newr < row and 0 <= newc < col and room[newr][newc] != 1:
                r = newr
                c = newc
                if room[r][c] == 0:
                    res += 1
                    room[r][c] = -1
            else:
                state = (state + 1) % 4
            if (r, c, state) in visited:
                return res
            visited.add((r, c, state))

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfCleanRooms([[0,0,0],[1,1,0],[0,0,0]]))   # 7
    print(s.numberOfCleanRooms([[[0,0,0],[1,0,1],[0,0,0]]])) # 3



