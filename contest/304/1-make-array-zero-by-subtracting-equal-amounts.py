"""
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
"""

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

    def minimumOperations(self, nums: List[int]) -> int:
        # Same elements, are always same
        # Different elements, are always different until 0
        # count different numbers
        return len(set(nums) - {0})

if __name__ == '__main__':
    s = Solution()
    print(s.minimumOperations([1,5,0,3,5])) # 3