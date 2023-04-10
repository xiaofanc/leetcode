
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # Recall that the operation only allows us 'move' values forward, so the previous smallest possible maximum value we have obtained can't be further reduced by the following numbers.
        res = 0
        prefixsum = 0
        for i in range(len(nums)):
            prefixsum += nums[i]
            curmax = math.ceil(prefixsum / (i+1))
            res = max(res, curmax)
        return res
            