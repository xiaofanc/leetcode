"""
create a new matrix with 0, and update the matrix with the paths at each point.
first row: only one path to each point, update all to 1
first col: only one path to each point, update all to 1
calculate the middle of matrix by adding the path from the left and the path from 
the up

3*3

[[0,0,0]
 [0,0,0]
 [0,0,0]]

[[1,1,1]
 [1,2,3]
 [1,3,6]]

"""
from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*m
        print(row)
        for i in range(n-1):
            # add 1 in the beginning for each row - only one method to get down
            next_row = [1] 
            for j in range(1, m):
                # add the methods from left and up
                next_row.append(next_row[-1] + row[j])
            row = next_row
            print(row)
        return row[-1]

    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0]*m for _ in range(n)]
        print(matrix)
        for i in range(m):
            matrix[0][i] = 1
        for j in range(n):
            matrix[j][0] = 1
        print(matrix)
        for i in range(1,m):
            for j in range(1,n):
                matrix[j][i] = matrix[j][i-1] + matrix[j-1][i]
        return matrix[-1][-1]


    def uniquePaths(self, m: int, n: int) -> int:
        def fcr(n, r):
            f = factorial
            return f(n) // (f(r)*f(n-r))
        return fcr(m+n-2, m-1)

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3) == 28)