"""
LC 775.
You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].
The number of global inversions is the number of the different pairs (i, j) where:
0 <= i < j < n
nums[i] > nums[j]
The number of local inversions is the number of indices i where:
0 <= i < n - 1
nums[i] > nums[i + 1]
Return true if the number of global inversions is equal to the number of local inversions.

If A[i] > min(A[i+2:]) then number of global inversions > local inversions.

Let's iterate through A from right to left, remembering the minimum value we've seen. If we remembered the minimum floor = min(A[i:]) and A[i-2] > floor, then we should return False
"""

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        min_num = len(nums)
        for i in range(len(nums)-1, 1, -1):
            min_num = min(min_num, nums[i])
            if nums[i-2] > min_num:
                return False
        return True

"""
If the 0 occurs at index 2 or greater, then A[0] > A[2] = 0 is a non-local inversion. So 0 can only occur at index 0 or 1. If A[1] = 0, then we must have A[0] = 1 otherwise A[0] > A[j] = 1 is a non-local inversion. Otherwise, A[0] = 0. To recap, the possibilities are either A = [0] + (ideal permutation of 1...N-1) or A = [1, 0] + (ideal permutation of 2...N-1).
A necessary and sufficient condition for these possibilities is that Math.abs(A[i] - i) <= 1. So we check this for every i.
"""
    def isIdealPermutation(self, A):
        return all(abs(i-x) <= 1 for i,x in enumerate(A))

if __name__ == '__main__':
	s = Solution()
	print(s.isIdealPermutation([1,0,2])) # True
	print(s.isIdealPermutation([2,1,0])) # False




