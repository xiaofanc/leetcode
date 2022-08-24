"""
sol1: backtrack - TLE
Given an unsorted array of integers, find the length of longest increasing subsequence.

sol2: split into sub problems
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

sol3: backwards
LIS[i] = longest increasing subsequence that starts with nums[i]
    [1,2,4,3]
LIS[3] = 1
LIS[2] = 1
LIS[1] = max(1, 1+LIS[2], 1+LIS[3]) = 2
LIS[0] = max(1, 1+LIS[1], 1+LIS[2], 1+LIS[3]) = 3
"""

class Solution: # time: O(n^2)
    # L[i]: longest increasing subsequence that ends with nums[i]
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        L = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):  # look back to check the longest subsequence before
                if nums[i] > nums[j] and L[i] < L[j]+1:
                    L[i] = L[j]+1
        return max(L)

    # LIS[i] = longest increasing subsequence that starts with nums[i]
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)

    """
    It appears the best way to build an increasing subsequence is: for each element num, if num is greater than the largest element in our subsequence, then add it to the subsequence. Otherwise, perform a linear scan through the subsequence starting from the smallest element and replace the first element that is greater than or equal to num with num. This opens the door for elements that are greater than num but less than the element replaced to be included in the sequence.
    """
    # Time: O(nlogm)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        seq = []
        for num in nums:
            i = bisect_left(seq, num)
            # if num is greater than the largest element in our subsequence
            if i == len(seq):
                seq.append(num)
            # replace the first element that is greater than or equal to num
            else:
                seq[i] = num
        return len(seq)

    # TLE
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        def backtrack(index, comb):
            nonlocal res
            res = max(res, len(comb))
            # print("comb->", comb[:])
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                if comb == [] or nums[i] > comb[-1]:
                    comb.append(nums[i])
                    # print("comb", comb)
                    backtrack(i+1, comb)
                    comb.pop()
        backtrack(0, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))  # 4: [2,3,7,101]




