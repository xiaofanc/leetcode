from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumn = sum(nums)
        suml, sumr = 0, sumn
        for i in range(len(nums)):
            sumr -= nums[i]
            if suml == sumr:
                return i
            suml += nums[i]
        return -1
            
if __name__ == '__main__':
	s = Solution()
	print(s.pivotIndex([1, 7, 3, 6, 5, 6]))