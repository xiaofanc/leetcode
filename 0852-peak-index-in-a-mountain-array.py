class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = A.index(max(A))
        for j in range(0, i):
            if A[j] >= A[j+1]:
                return None
        for k in range(i, len(A)-2):
            if A[k] <= A[k+1]:
                return None
        return i
        
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # [0, 2, 1, 0]
        # The point that it stops increasing is the peak
        for i in range(len(A)):
            if A[i] > A[i+1]:
                return i

    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # binary search to find the largest index i
        left, right = 0, len(A)-1
        while left < right:
            mid = (left+right) / 2
            if A[mid] < A[mid+1]:
                left = mid+1
            else:
                right = mid
        return left

if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray([0,2,1,0]) == 1)




