
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        right, down = len(matrix[0])-1, len(matrix)-1
        left, up = 0, 0
        res = []
        while left <= right and up <= down:
            if left == right:
                for i in range(up, down+1):
                    res.append(matrix[i][left])
            elif up == down:
                for j in range(left, right+1):
                    res.append(matrix[up][j])
            else:
                # first step: iterate the up row from left to right
                for i in range(left, right):
                    res.append(matrix[up][i])
                # second step: iterate the right col from up to down
                for j in range(up, down):
                    res.append(matrix[j][right])
                # third step: iterate the bottem row from right to left
                for m in range(right, left, -1):
                    res.append(matrix[down][m])
                # fourth step: iterate the left col from bottem to top
                for n in range(down, up, -1):
                    res.append(matrix[n][left])
            # break
            print("before", left, right, up, down)
            left += 1
            right -= 1
            up += 1
            down -= 1
            print("after", left, right, up, down)

        return res 

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(s.spiralOrder(matrix)) # == [1,2,3,6,9,8,7,4,5]
