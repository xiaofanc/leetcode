"""
start from water to visit nodes that can be reachable
从四周向内visit，找到pacific和atlantic water可以到的点，求集合。
从四周向内递增时才可以到达。
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(r, c, visited, preHeight):
            # if node is in the visited set or out of bounds or not reachable, return
            if (r,c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < preHeight:
                return
            # (r,c) is reachable and find the neighbors with height > heights[r][c]
            visited.add((r,c))
            for dx, dy in dirs:
                dfs(r+dx, c+dy, visited, heights[r][c])
        
        # base case: pacific can reach the first row and the first col
        # base case: atlantic can reach the last row and the last col
        for j in range(cols):
            dfs(0, j, pac, heights[0][j])
            dfs(rows-1, j, atl, heights[rows-1][j])
        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols-1, atl, heights[i][cols-1])
        
        # find the intersection
        return list(pac.intersection(atl))

if __name__ == '__main__':
    s = Solution()
    # [[4,0],[0,4],[3,1],[1,4],[3,0],[2,2],[1,3]]
    print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))




                