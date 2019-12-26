from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for _ in range(len(triangle)-1):
            last = triangle.pop()
            triangle[-1] = [min(i,j) + k for i, j, k in zip(last[1:], last[0:-1], triangle[-1])]
        return triangle[0][0]

if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]) == -1)