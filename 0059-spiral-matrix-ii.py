
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, up, down = 0, n-1, 0, n-1
        count = 1
        res = [[0]*n for i in range(n)]
        mid = n // 2
        while left < right and up < down:
            for j in range(left, right): # [left, right)
                res[up][j] = count
                count += 1
            for i in range(up, down):
                res[i][right] = count
                count += 1
            for j in range(right,left,-1):
                res[down][j] = count
                count += 1
            for i in range(down,up,-1):
                res[i][left] = count
                count += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        if n % 2: 
            res[mid][mid] = count
        return res

# Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n. Make a right turn when the cell ahead is already non-zero.
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0]*n for i in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k+1
            # turn direction in the end -> [0,0] is populated
            if A[(i+di) % n][(j+dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A

if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3)) # [[1,2,3],[8,9,4],[7,6,5]]
