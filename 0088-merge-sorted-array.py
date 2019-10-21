class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O(m+n): nums1[:] = sorted(nums1[:m] + nums2)
        nums1_copy = nums1[:m]
        nums1[:] = []
        
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
            
        if p1 < m:
            nums1[p1+p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1+p2:] = nums2[p2:]
        return nums1

s=Solution()
print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))