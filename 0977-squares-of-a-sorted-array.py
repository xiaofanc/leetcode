

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res = [0] * len(nums)
        for i in range(r, -1, -1):
            if abs(nums[l]) <= abs(nums[r]):
                res[i] = abs(nums[r]) * abs(nums[r])
                r -= 1
            else:
                res[i] = abs(nums[l]) * abs(nums[l])
                l += 1
        return res

if __name__ == "__main__":
	s = Solution()
	print(s.sortedSquares([-4,-1,0,3,10])) # [0,1,9,16,100]