class Solution:
    # O((m+n)log10^10)
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # we binary-search for a value m from 0-10**10, count products less than m, and return the smallest value where the number of products is exactly k.
        m, n = len(nums1), len(nums2)
        A1, A2 = [-n for n in nums1 if n < 0][::-1], [n for n in nums1 if n >= 0]
        B1, B2 = [-n for n in nums2 if n < 0][::-1], [n for n in nums2 if n >= 0]
        
        neg = len(A1)*len(B2) + len(A2)*len(B1)
        if neg < k:
            # res is positive, update k
            k -= neg
            s = 1
        else:
            # res is negative, update k for searching positive numbers
            k = neg-k+1
            B1, B2 = B2, B1
            s = -1
        
        def count(A, B, x):
            # count pairs that make A[i]*B[j] <= x in linear time: O(m+n)
            # numbers in A and B are all positive numbers, sorted
            res = 0
            j = len(B)-1
            for i in range(len(A)):
                while j >= 0 and A[i]*B[j] > x:
                    j -= 1
                res += j+1
            return res
        
        left, right = 0, 10**10 # nums1[i], nums2[j] <= 10^5
        while left < right:
            m = left + (right-left) // 2
            # find the min m that makes number of pairs == k
            if count(A1, B1, m) + count(A2, B2, m) >= k:
                right = m
            else:
                left = m+1
        # left is the smallest number that makes number of pairs == k
        return left * s
                    
            
            
        
        