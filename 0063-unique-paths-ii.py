"""
create a new matrix with 0, and update the matrix with the paths at each point.
first row: only one path to each point, update as 1, if meeting obstacle then 
no need to update afterwards since we can not get that point
first col: only one path to each point, update as 1, if meeting obstacle then no
need to update afterwards since we can not get that point

calculate the middle of matrix by adding the path from the left and the path from 
the up, if meeting obstacle at one point, then no need to update it (still 0)

3*3

[[0,0,0]
 [0,1,0]
 [0,0,0]]

[[1,1,1]
 [1,0,1]
 [1,1,2]]

3*3

[[0,1,0]
 [0,0,0]
 [0,0,0]]

[[1,0,0]
 [1,1,1]
 [1,2,3]]

"""
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width, height = len(obstacleGrid[0]), len(obstacleGrid)
        matrix = [[0]*width for _ in range(height)]
        for i in range(width):
            if obstacleGrid[0][i] == 1:
                break
            matrix[0][i] = 1
        for j in range(height):
            if obstacleGrid[j][0] == 1:
                break
            matrix[j][0] = 1
        print(matrix)
        for i in range(1,width):
            for j in range(1,height):
                print(j, i)
                if obstacleGrid[j][i] == 1:
                    continue
                matrix[j][i] = matrix[j-1][i] + matrix[j][i-1]
        print(matrix)
        return matrix[-1][-1]


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width, height = len(obstacleGrid[0]), len(obstacleGrid)
        row_start_obs = False  # next rows below this row will be 0
        row = [0]*width
        if obstacleGrid[0][0] == 1: return 0  # cannot start
        for j in range(width):
            if obstacleGrid[0][j] == 1:       # if there is 1 in the first row
                break                         # jump out of the for loop
            row[j] = 1
            #print(row)
        for i in range(1, height):            
            # new row start point is not an obstacle
            if obstacleGrid[i][0] == 0 and row_start_obs == False:
                new_row = [1]   

            # new row start point is an obstacle or have met obstacle in the previous start point
            elif obstacleGrid[i][0] == 1 or row_start_obs == True:
                row_start_obs = True
                new_row = [0]

            # obstacle in the middle
            for j in range(1, width):
                if obstacleGrid[i][j] == 1:  
                    new_row.append(0)
                else:
                    new_row.append(new_row[-1] + row[j])

            row = new_row
            print(row)
        return row[-1]

if __name__ == '__main__':
    s = Solution()
    #assert s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2)
    print(s.uniquePathsWithObstacles([[0,1,0],[0,0,0],[0,0,0]]) == 3)




