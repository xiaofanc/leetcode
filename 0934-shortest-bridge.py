class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        # find the root of the first island
        def first():
            for i in range(height):
                for j in range(width):
                    if grid[i][j] == 1:
                        return (i,j)
        # find all points of the first island            
        def dfs(i, j):
            grid[i][j] = -1
            bfs.append((i, j))
            for new_x, new_y in ((i+1, j),(i-1, j),(i, j+1),(i, j-1)):
                if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] == 1:
                    dfs(new_x, new_y)
        # find the first island and marked as visited, store the points in bfs
        bfs = []
        dfs(*first())
        # print(bfs)
        # print(grid)
        step = 0
        while bfs:
            new = []
            for i, j in bfs:
                for new_x, new_y in ((i+1, j),(i-1, j),(i, j+1),(i, j-1)):
                    if 0 <= new_x < height and 0 <= new_y < width:
                        if grid[new_x][new_y] == 1:
                            return step
                        # else - time limit exceeded (include -1)
                        # not grid[new_x][new_y] = (grid[new_x][new_y] = 0) - not visited
                        elif not grid[new_x][new_y]:  
                            grid[new_x][new_y] = -1
                            new.append((new_x, new_y))
            # print(new)
            step += 1
            bfs = new
                                    
        return step
            
                

    def shortestBridge(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        # find the root of the first island
        def first():
            for i in range(height):
                for j in range(width):
                    if grid[i][j] == 1:
                        return (i,j)
        # find all points of the first island            
        def dfs(i, j):
            grid[i][j] = -1
            bfs.append((i, j))
            for new_x, new_y in ((i+1, j),(i-1, j),(i, j+1),(i, j-1)):
                if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] == 1:
                    dfs(new_x, new_y)
        # find the first island and marked as visited, store the points in bfs
        bfs = []
        dfs(*first())
        # print(bfs)
        # print(grid)
        step = 0
        while bfs:
            new = []
            for i, j in bfs:
                for new_x, new_y in ((i+1, j),(i-1, j),(i, j+1),(i, j-1)):
                    if 0 <= new_x < height and 0 <= new_y < width:
                        if grid[new_x][new_y] == 1:
                            return step
                        # else - time limit exceeded (include -1)
                        # not grid[new_x][new_y] = (grid[new_x][new_y] = 0) - not visited
                        elif not grid[new_x][new_y]:  
                            grid[new_x][new_y] = -1
                            new.append((new_x, new_y))
            # print(new)
            step += 1
            bfs = new
                                    
        return step
            
if __name__ == '__main__':
    s = Solution()
    print(s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))  #2           
        