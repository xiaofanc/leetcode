# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

from typing import List

class Solution:
    # Time = O(n); Space = O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        j = -1 # why? for the case when the input is in descending order like [3,2,1] -> [1,2,3]
        # find the first decreasing element backwards
        while i > 0:
            if nums[i-1] < nums[i]:
                j = i-1 # j = 3 in this case
                break # break while loop
            i -= 1 
            #print(i)
        # find the first number just larger than the first decreasing element among the numbers lying to its right section
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]:
                # swap
                # [1, 5, 8, 5, 7, 6, 4, 3, 1]
                nums[i], nums[j] = nums[j], nums[i]
                #print(nums)
                # [1, 5, 8, 5, 1, 3, 4, 6, 7]
                # sort in ascending order after the node
                nums[j+1:] = sorted(nums[j+1:])
                #print(nums)
                return nums
                
if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([1,5,8,4,7,6,5,3,1]))  #[1,5,8,5,1,3,4,6,7]
    print(s.nextPermutation([1,8,5,4,7,6,5,3,1]))  #[1,8,5,5,1,3,4,6,7]





