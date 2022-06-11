"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
"""
class Solution:
    # Time: O(MxN), Sapce: O(M+N)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = [1]*m, [1]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0
        for i in range(m):
            if rows[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if cols[j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
if __name__ == '__main__':
    s = Solution()
    print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))                
                    
                