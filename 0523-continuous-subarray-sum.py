"""
If k == 0, then search for any consecutive pair of 0s.
if k == 0: return any(nums[i] == 0 and nums[i + 1] == 0 for i in xrange(len(nums) - 1))
else:
    we will keep track of indices of the cumulative sum (or prefix sum) mod by k in a dictionary. We will return True if we've seen a cumulative sum % k at least 2 indices before.
"""

class Solution:
    # brute force: O(n^2)-TLE
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for start in range(len(nums)):
            s = 0
            for end in range(start, len(nums)):
                s += nums[end]
                # print("s->", s)
                if end - start >= 1 and s % k == 0:
                    return True
        return False

    # TLE - 94/96
    # store previous subsum s[:j]:j in the dict
    # check if (s[:i]-s[:j]) % k == 0 and i-j >= 2
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        subsum = {0:-1} # store subsum:i
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            for sub, j in subsum.items():
                if i-j >= 2 and (s-sub) % k == 0:
                    return True
            if s not in subsum:
                subsum[s] = i
            # print("subsum->", subsum)
        return False

    # if sum(nums[:j]) % k = d and sum(nums[:i]) % k == d
    # then sum_i = n*k+d, sum_j = m*k+d
    # so sum_i-sum_j = (n-m)*k
    # so we only need to store subsum % k as the key, index as value
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumMod = {0:-1} # store subsum % k :i
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k in sumMod: 
                if i-sumMod[s%k] >= 2:
                    return True
            else:  # there can be multiple subsum map to same mod, only store the first i
                sumMod[s%k] = i
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([23,2,6,4,7], 13)) # False
    print(s.checkSubarraySum([23,2,6,4,7], 25)) # True







