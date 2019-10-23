from typing import List
class Solution:
    def floodFill0(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        height, width = len(image), len(image[0])
        deltas = [(0,1),(1,0),(0,-1),(-1,0)]
        source_color = image[sr][sc]
        def color(x,y):
            if 0 <= x < height and 0 <= y < width:
                return image[x][y]
        def dfs(x,y):
            image[x][y] = newColor
            for dx, dy in deltas:
                nx, ny = x+dx, y+dy
                if color(nx,ny) == source_color:
                    dfs(nx, ny)
        if newColor != source_color:
            dfs(sr,sc)
        return image

        #if newColor != source_color:
        #    dfs(sr,sc)
        #    return image
        #else: 
        #    return image
    
    def floodFill1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r,c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1,c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r,c-1)
                if c+1 < C: dfs(r, c+1)
        dfs(sr, sc)
        return image

s=Solution()
print(s.floodFill0([[0,0,1],[0,1,1]], 1, 1, 2))
print(s.floodFill1([[0,0,1],[0,1,1]], 1, 1, 2))
    
    