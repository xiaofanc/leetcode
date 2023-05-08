
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        res = [set(),set()]
        for n in nums1:
            if n not in s2:
                res[0].add(n)
        for n in nums2:
            if n not in s1:
                res[1].add(n)
        return res