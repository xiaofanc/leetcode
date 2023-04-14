class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = float("inf")
        res = min(res, nums1[0]*10+nums2[0], nums2[0]*10+nums1[0])
        
        # find the first number exist in both arr
        a, b = 0, 0
        while a < len(nums1) and b < len(nums2):
            if nums1[a] < nums2[b]:
                a += 1
            elif nums1[a] > nums2[b]:
                b += 1
            else:
                res = min(res, nums1[a])
                break
        return res
                
        
        