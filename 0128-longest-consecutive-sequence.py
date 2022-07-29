"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Time: O(n) why?
For those who got confused by if the last solution is O(n^2) or O(n), please take a close look at the entering of the logic: if(!num_set.contains(num-1)).
That means, for example, 6,5,4,3,2,1 input, only the value 1 is valid for the loop(all other values have its value - 1 in the set), that is O(n).
Another corner example, 2, 5, 6, 7, 9, 11. All of these numbers are the "entrance" for the logic but the while loop doesn't run much. That is O(n) as well.

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # make look-up O(1)
        longest = 0
        for n in nums:
            # check if it is the start of a seq
            # only continue when it is a start
            if n-1 not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
                
if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2])) # 4
    print(s.longestConsecutive([0]))  # 1
    print(s.longestConsecutive([]))   # 0