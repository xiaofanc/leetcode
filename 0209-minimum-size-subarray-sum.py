"""
sliding window:
窗口就是 满足其和 ≥ s 的长度最小的 连续 子数组。
窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。
窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，窗口的起始位置设置为数组的起始位置就可以了。

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        minlen = float("inf")
        while j < len(nums):
            s = sum(nums[i:j+1])
            if s >= target:
                minlen = min(minlen, j-i+1)
                i += 1
            else:
                j += 1
        return minlen if minlen != float("inf") else 0

    # Time: O(n), space: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        s = 0
        minlen = float("inf")
        for j in range(len(nums)):
            s += nums[j]
            while s >= target:
                minlen = min(minlen, j-i+1)
                s -= nums[i]
                i += 1
        return minlen if minlen != float("inf") else 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums = [0] + nums
        s = list(itertools.accumulate(nums))
        left = 0
        minlen = float("inf")
        for right in range(1, len(s)):
            while s[right] - s[left] >= target:
                minlen = min(minlen, right-left)
                left += 1
        return minlen if minlen != float("inf") else 0
        
if __name__ == '__main__':
	s = Solution()
	print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
	print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
	print(s.minSubArrayLen(15, [1,2,3,4,5]))



