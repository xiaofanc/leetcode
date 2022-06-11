"""
rotate the image by 90 degrees (clockwise).
solution: update the matrix anti-clockwise.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1
        while l < r:
            top, bottom = l, r
            # rotate element 0 to r-l
            for i in range(r-l): 
                # get the top left element
                topLeft = matrix[top][l+i]
                
                # move bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l]
                
                # move bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                # move top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # move top left to top right
                matrix[top+i][r] = topLeft
            # update the layer
            l += 1
            r -= 1
        return matrix
        
if __name__ == '__main__':
	s = Solution()
	print(s.rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]
	print(s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]





