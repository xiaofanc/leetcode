from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [None for _ in range(i+1)] # create empty space for each row
            row[0], row[-1] = 1, 1           # put 0 to the head and the end of the row
            for j in range(1,len(row)-1):    # calculate element 1:-2
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)             # will append row 0 and row 1 first
        return triangle

s=Solution()
print(s.generate(5))
print(s.generate(8))
print(s.generate(10))