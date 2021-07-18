class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        
        height, width = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # points pacific reachable
        pacific = set()
        # points atlantic reachable
        atlantic = set()

        def dfs(x, y, reachable):
            reachable.add((x,y))

            for dx, dy in directions:
                new_row, new_col = x+dx, y+dy
                if new_row < 0 or new_row >= height or new_col < 0 or new_col >= width:
                    continue
                # check if the new cell has a higher or equal height so that water can flow
                if heights[new_row][new_col] < heights[x][y]:
                    continue
                if (new_row, new_col) in reachable:
                    continue
                dfs(new_row, new_col, reachable)
        
        # initialize      
        for i in range(height): 
            dfs(i, 0, pacific)
            dfs(i, width-1, atlantic)
        for j in range(width):
            dfs(0, j, pacific)
            dfs(height-1, j, atlantic)
        
        # reachable by both
        return list(pacific.intersection(atlantic))

if __name__ == '__main__':
    s = Solution()
    # [[4,0],[0,4],[3,1],[1,4],[3,0],[2,2],[1,3]]
    print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))




                