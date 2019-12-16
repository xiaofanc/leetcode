class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key = lambda x: x % 2)
        return A
            
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B, C = [], []
        for num in A:
            if num % 2 == 0:
                B.append(num)
            else:
                C.append(num)
        return B + C

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return ([x for x in A if x % 2 == 0]) + ([x for x in A if x % 2 == 1])

    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A)-1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A


if __name__ == '__main__':
	s = Solution()
	print(s.sortArrayByParity([3,1,2,4]))