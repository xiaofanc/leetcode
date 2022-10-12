
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-3,-1,-1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

if __name__ == '__main__':
	s = Solution()
	print(s.largestPerimeter([2,1,2])) # 5
	print(s.largestPerimeter([1,1,2])) # 0
                
            