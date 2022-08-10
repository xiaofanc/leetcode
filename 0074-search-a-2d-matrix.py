"""
binary search a target in the 2D matrix
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # seach which rows to check first
        # find the largest number <= target
        def findRow(l, r):
            while l <= r:
                m = l + (r-l) // 2
                if matrix[m][0] == target:
                    return m
                elif matrix[m][0] > target:
                    r = m - 1
                else:
                    l = m + 1
            return r
        
        row = findRow(0, rows-1)
        
        # find target in the row
        def findTarget(l, r):
            while l <= r:
                m = l + (r-l) // 2
                if matrix[row][m] == target:
                    return True
                elif matrix[row][m] > target:
                    r = m - 1
                else:
                    l = m + 1
        
        # search cols in the row
        return findTarget(0, cols-1)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        if row == 0 and col == 0:
            return matrix[0][0] == target
        rows = [matrix[i][0] for i in range(row)]
        # search for row
        # i is the place that target can be inserted, matrix[i][0] >= target
        i = bisect.bisect_left(rows, target)
        
        if i == 0:
            return matrix[0][0] == target
        elif i == row:
            i -= 1
        else:
            if matrix[i][0] != target:
                i -= 1
            else:
                return True
        
        # search for col        
        cols = [matrix[i][j] for j in range(col)]
        j = bisect.bisect_left(cols, target)
        if j < col and matrix[i][j] == target:
            return True
        return False
        
if __name__ == '__main__':
	s = Solution()
	print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))        
    print(s.searchMatrix([[1]], 2))        


	
