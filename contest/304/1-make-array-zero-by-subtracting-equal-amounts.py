

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while max(nums) != 0:
            minn = float('inf')
            for n in nums:
                if n != 0:
                    minn = min(minn, n)
            for i, n in enumerate(nums):
                if n != 0:
                    nums[i] -= minn
            cnt += 1
        return cnt
                
            
            