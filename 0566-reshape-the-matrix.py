class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[None for i in range(c)] for j in range(r)]
        rows, cols = len(mat), len(mat[0])
        if (r * c != rows * cols):
            return mat
        i, j = 0, 0
        for m in range(rows):
            for n in range(cols): 
                res[i][j] = mat[m][n]
                j += 1
                if j == c:
                    i += 1
                    j = 0
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.matrixReshape([[1,2],[3,4],[5,6]])) # [[1,2,3],[4,5,6]]