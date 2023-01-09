class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        # find the first number >= 0        
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] < 0:
                l = m+1
            else:
                r = m
        # nums[l] is the first >= 0
        zero = 0
        for i in range(l, len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] > 0:
                break
        return max(l, len(nums)-l-zero)

    def maximumCount(self, nums: List[int]) -> int:
        # the first num >= 0
        neg = bisect.bisect_left(nums, 0)
        # bisect.bisect_right(nums, 0) return the first num > 0
        pos = len(nums) - bisect.bisect_right(nums, 0)

        return max(neg, pos)




        