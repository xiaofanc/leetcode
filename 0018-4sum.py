"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

[-2,-1,-1,1,1,2,2], 0
res: [[-2,-1,1,2],[-1,-1,1,1]]

[2,2,2,2,2], 8
res: [[2,2,2,2]]

"""

class Solution:
	# Time: O(n^(k-1)) = O(n^3)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n-3):
            # print("i, nums[i]", i, nums[i])
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, n-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res


class Solution:
	# Time: O(n^(k-1))
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums, target, k):
            res = []
            if not nums:
                return res
            avg_value = target // k
            if nums[0] > avg_value or nums[-1] < avg_value:
                return res
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]] + subset)
            return res
                
        
        def twoSum(nums, target):
            # nums is already sorted
            res = []
            l, r = 0, len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
            return res
        
        nums.sort()
        return kSum(nums, target, 4)
                    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def ksum(nums, target, k):
            res = []
            if not nums:
                return res
            if len(nums) < k:
                return res
            avgv = target // k
            if nums[0] > avgv or nums[-1] < avgv:
                return res
            if k == 2:
                return twosum(nums, target)
            
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                for subset in ksum(nums[i+1:], target-nums[i], k-1):
                    res.append([nums[i]] + list(subset))
            return res
            
        
        def twosum(nums, target):
            dct = {}
            res = set()
            for i in range(len(nums)):
                if target-nums[i] in dct:
                    res.add((nums[i], target-nums[i]))
                else:
                    dct[nums[i]] = i
            return res
        
        nums.sort()
        return ksum(nums, target, 4)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def nsum(nums, n, start, target):
            size = len(nums)
            res = []
            # at least two sum and have enough nums
            if n < 2 or size < n:
                return res
            # base case: 2sum
            if n == 2:
                l, r = start, size-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        res.append([nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
            else:
                # n > 2，递归计算(n-1)sum
                for i in range(start, size):
                    # 第一个数不能重复 -> i > start !!!!!!
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    sub = nsum(nums, n-1, i+1, target-nums[i])
                    for s in sub:
                        s.append(nums[i])
                        res.append(s)
            return res
        return nsum(nums, 4, 0, target)


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def twosum(nums, target):
            res = []
            l, r = 0, len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            return res

        def nsum(nums, n, target):
            res = []
            # print("nums ", nums)
            # at least two sum and have enough nums
            if n < 2 or len(nums) < n:
                return res
            # base case: 2sum
            if n == 2:
                return twosum(nums, target)
            else:
                # n > 2，递归计算(n-1)sum
                for i in range(len(nums)):
                    # 第一个数不能重复
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    sub = nsum(nums[i+1:], n-1, target-nums[i])
                    for s in sub:
                        s.append(nums[i])
                        res.append(s)
            return res
        return nsum(nums, 4, target)

if __name__ == '__main__':
	s = Solution()
	print(s.fourSum([-2,-1,-1,1,1,2,2], 0)) # [[-2,-1,1,2],[-1,-1,1,1]]
	print(s.fourSum([2,2,2,2,2], 8))   # [[2,2,2,2]]


