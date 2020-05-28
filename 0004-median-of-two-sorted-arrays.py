class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i == len(nums1): nums.extend(nums2[j:])
        if j == len(nums2): nums.extend(nums1[i:])
        return (nums[l//2-1] + nums[l//2])/2 if l % 2 == 0 else nums[l//2]
        
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3],[2]))