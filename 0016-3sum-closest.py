"""
find the sum of three integers cloest to the target
"""

class Solution:
	# Time: O(nlogn + n^2), Space depends on sort
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # print(nums)
        res = 0
        n = len(nums)
        diff = float("inf")
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            # print("i, l, r ->", i, l, r)
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
                # print("diff, res ->", diff, res)
        return res

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # print(nums)
        n = len(nums)
        diff = float("inf")
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target - s) < abs(diff):
                    diff = target - s
                if s < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0:
                break
        return target - diff

if __name__ == '__main__':
	s = Solution()
	print(s.threeSumClosest([1,1,1,0], -100))  # 2