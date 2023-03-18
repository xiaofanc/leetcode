class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        s = 0
        cnt = 0 
        for i, n in enumerate(nums):
            s += n
            if s > 0:
                cnt += 1
            else:
                break
        return cnt
        