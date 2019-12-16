from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def reverse(element):
            l, r = 0, len(element)-1
            while l < r:
                element[l], element[r] = element[r], element[l]
                l += 1
                r -= 1
            return element
        def invert(element):
            for i in range(len(element)):
                if element[i] == 0: element[i] = 1
                else: element[i] = 0
            return element
        for i in range(len(A)):
            A[i] = reverse(A[i])
            print(A[i])
            A[i] = invert(A[i])
            print(A[i])
        return A

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        A = [[0 if i == 1 else 1 for i in reversed(a)] for a in A]
        return A

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m = {0:1, 1:0}
        A = [[m[i] for i in reversed(a)] for a in A]
        return A

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in A:
            result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return result

        
if __name__ == '__main__':
    s = Solution()
    print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))



    