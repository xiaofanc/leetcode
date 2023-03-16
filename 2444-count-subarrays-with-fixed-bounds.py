class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # calculate the subarray ends in i
        # keep track of the most recent minK and maxK for i
        # keep track of the most recent value out of range 
        maxpos, minpos, leftBound = -1, -1, -1
        res = 0
        for i in range(len(nums)):
            if nums[i] == minK:
                minpos = i
            if nums[i] == maxK:
                maxpos = i
            if nums[i] < minK or nums[i] > maxK:
                leftBound = i
            # the number of valid subarray ends in i equals the number of elements between leftBound and the smaller of the two most recent positions.
            # why smaller? so that we can make sure minK and maxK is in the subarray
            res += max(0, min(minpos, maxpos)-leftBound)
        return res