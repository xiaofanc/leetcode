"""
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
"""
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0]*m
        cols = [0]*n
        idxes = {}
        for i in range(m):
            for j in range(n):
                idxes[mat[i][j]] = (i, j)
        
        for i in range(len(arr)):
            r, c = idxes[arr[i]]
            rows[r] += 1
            cols[c] += 1
            # print("rows, cols ", rows, cols)
            if rows[r] == n:
                return i
            if cols[c] == m:
                return i
            
            
        