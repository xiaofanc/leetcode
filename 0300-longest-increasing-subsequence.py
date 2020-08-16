"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

L[i] = the longest increasing subsequence which must include nums[i] in the end

    [10,9,2,5,3,7,101,18]
L = [1,1,1,2,2,?....]
i = 5:
j = 2 nums[5](7) > nums[2](2) and 1 < 1+1: L[5] = 2     {2,7}
j = 3 nums[5](7) > nums[3](5) and 2 < 2+1: L[5] = 3     {2,5,7}
j = 4 nums[5](7) > nums[4](3) and 3   2+1: same length  {2,3,7}

"""

class Solution: # time: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        L = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):  # look back to check the longest subsequence before
                if nums[i] > nums[j] and L[i] < L[j]+1:
                    L[i] = L[j]+1
        return max(L)

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))  # 4: [2,3,7,101]