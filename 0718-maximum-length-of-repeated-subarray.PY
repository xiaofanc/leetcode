"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(len(nums1)-1,-1,-1):
            for j in range(len(nums2)-1,-1,-1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(row) for row in dp)
                
if __name__ == '__main__':
	s = Solution()
	print(s.findLength([1,2,3,2,1],[3,2,1,4,7]))  # 3

