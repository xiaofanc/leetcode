"""
Input: matrix = 
[[1,4,7,11,15],
 [2,5,8,12,19],
 [3,6,9,16,22],
 [10,13,14,17,24],
 [18,21,23,26,30]], 

 target = 5

"""
class Solution:
	# Time: O(m+n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        i, j = rows-1, 0
        
        # start from the bottom left
        while 0 <= i < rows and 0 <= j < cols: 
            # if num > target: move up
            if matrix[i][j] > target:
                i -= 1
            # if num < target: move right
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

    # Time: O(logmn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        # binary search rows
        def searchRows(l, r):
            while l <= r:
                m = l + (r-l) // 2
                if matrix[m][0] == target:
                    return m
                elif matrix[m][0] > target:
                    r = m - 1
                else:
                    l = m + 1
            return r
        
        row = searchRows(0, rows-1)
        
        def searchCols(l, r):
            while l <= r:
                m = l + (r-l) // 2
                if matrix[0][m] == target:
                    return m
                elif matrix[0][m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return r
        
        col = searchCols(0, cols-1)
        
        for i in range(row+1):
            for j in range(col+1):
                if matrix[i][j] == target:
                    return True
        
        return False

	# Time: O(logmn)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        def binarySearch(l, r, start, vertical):
            # search col if vertical
            if vertical:
                while l <= r:
                    m = l + (r-l) // 2
                    if matrix[start][m] == target:
                        return True
                    elif matrix[start][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                while l <= r:
                    m = l + (r-l) // 2
                    if matrix[m][start] == target:
                        return True
                    elif matrix[m][start] > target:
                        r = m - 1
                    else:
                        l = m + 1      
            return False
        
        for i in range(min(rows, cols)):
            vertical = binarySearch(0, cols-1, i, True)
            horizontal = binarySearch(0, rows-1, i, False)
            if vertical or horizontal:
                return True
        return False

if __name__ == '__main__':
	s = Solution()
	print(s.searchMatrix([[-5]], -5))  # True
	


