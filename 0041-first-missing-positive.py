"""
Now everything is ready to write down the algorithm.

Check if 1 is present in the array. If not, you're done and 1 is the answer.
Replace negative numbers, zeros, and numbers larger than n by 1s.
Walk along the array. Change the sign of a-th element if you meet number a. Be careful with duplicates : do sign change only once. Use index 0 to save an information about presence of number n since index n is not available.
Walk again along the array. Return the index of the first positive element.
If nums[0] > 0 return n.
If on the previous step you didn't find the positive element in nums, that means that the answer is n + 1.

"""

class Solution:
	# Time complexity : O(N) since all we do here is four walks along the array of length N.
	# Space: O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # check if 1 exists
        if 1 not in nums:
            return 1
        # replace neg, 0 and numbers > n by 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        # walk along the array, change the sign of a-th element if you meet a
        # If nums[2] is positive - number 2 is missing
        for num in nums:
            a = abs(num)
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
            
        print(nums)
        # nums[0] represents if n exits in the array
        # find the first positive element since nums[1:]
        for i in range(1, n):
            if nums[i] > 0:
                return i
        # check if n exists
        if nums[0] > 0:
            return n
        
        return n + 1
            
if __name__ == '__main__':
	s = Solution()
	print(s.firstMissingPositive([1,2,0])) #  3



