class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpmax = [0]*len(nums)
        dpmin = [0]*len(nums)
        dpmax[0], dpmin[0] = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            dpmax[i] = max(nums[i], dpmin[i-1]*nums[i], dpmax[i-1]*nums[i])
            dpmin[i] = min(nums[i], dpmin[i-1]*nums[i], dpmax[i-1]*nums[i])
            ans = max(ans, dpmax[i], dpmin[i])
            print(ans, dpmax[i], dpmin[i])
        return ans
            
    def maxProduct(self, nums: List[int]) -> int:
        hi, lo = 1, 1
        ans = nums[0]
        for n in nums:
            hi, lo = max(n, lo*n, hi*n), min(n, lo*n, hi*n)
            ans = max(ans, hi)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2,3,-2,4]) == 6)