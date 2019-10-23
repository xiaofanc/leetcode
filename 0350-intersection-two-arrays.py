from typing import List
import collections
class Solution:
    def intersect0(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        counter = collections.Counter(nums1)
        for char in nums2:
            if counter[char] > 0:
                res.append(char)
                counter[char] -= 1
        return res
    
    #method2: two pointers 
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        nums1, nums2 = sorted(nums1), sorted(nums2)
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        return [s for s in nums1 if s in nums2]


    #reomve duplicates
    def intersect10(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)

    def intersect11(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [x for x in nums1 if x in nums2]
    

s=Solution()
# keep duplicates
print(s.intersect0([1,2,2],[4,9,9,4,2,2]))
print(s.intersect1([1,2,2],[4,9,9,4,2,2]))
print(s.intersect2([1,2,2],[4,9,9,4,2,2]))
# remove duplicates with set
print(s.intersect10([1,2,2],[4,9,9,4,2,2]))
print(s.intersect11([1,2,2],[4,9,9,4,2,2]))