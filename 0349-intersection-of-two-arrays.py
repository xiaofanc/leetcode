
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
    
s = Solution()
print(s.intersection([1,2,2,1], [2,2])) # [2]