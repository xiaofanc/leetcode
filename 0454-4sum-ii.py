"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

do not need to consider duplicates

"""

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sumd = {}
        for n1 in nums1:
            for n2 in nums2:
                sumd[n1+n2] = sumd.get(n1+n2, 0) + 1
        
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                if -n3-n4 in sumd:
                    count += sumd[-n3-n4]
        return count

s = Solution()
print(s.fourSumCount([1,2], [-2,-1], [-1,2], [0,2])) # 2
