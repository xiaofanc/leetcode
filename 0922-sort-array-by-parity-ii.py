"""
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
"""

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i % 2 == 0 and nums[i] % 2 == 1:
                for j in range(i, len(nums)):
                    if j % 2 == 1 and nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
            
            if i % 2 == 1 and nums[i] % 2 == 0:
                for j in range(i, len(nums)):
                    if j % 2 == 0 and nums[j] % 2 == 1:
                        nums[i], nums[j] = nums[j], nums[i]               
                        break
        return nums

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2:
                while nums[j] % 2:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums
        
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        ans[::2] = (x for x in nums if x % 2 == 0)
        ans[1::2] = (x for x in nums if x % 2 == 1)
        return ans

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        t = 0
        for i, x in enumerate(nums):
            if x % 2 == 0:
                ans[t] = x
                t += 2
        t = 1
        for i, x in enumerate(nums):
            if x % 2 == 1:
                ans[t] = x
                t += 2
        return ans

if __name__ == '__main__':
	s = Solution()
	print(s.sortArrayByParityII([4,2,5,7])) # [4,5,2,7]



