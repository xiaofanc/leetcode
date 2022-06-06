"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            # check if it is the start of a seq
            if n-1 not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
                
if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))