from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        height, width = len(A), len(A[0])
        #ans = [[None]*height for _ in range(width)]
        ans = [[None for _ in range(height)] for _ in range(width)]
        for i in range(height):
            for j in range(width):
                ans[j][i] = A[i][j]
        return ans
    
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        print(A)
        return [list(a) for a in zip(*A)]

    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(A[0])):
            temp = []
            for j in range(len(A)):
                temp.append(A[j][i])
            res.append(temp)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.transpose([[1.0,2,3],[4,5,6]]))
    print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))