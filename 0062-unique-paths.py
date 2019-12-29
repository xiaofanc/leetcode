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

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3) == 28)