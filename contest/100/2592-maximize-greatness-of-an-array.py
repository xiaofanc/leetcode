"""
You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.

We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].

Return the maximum possible greatness you can achieve after permuting nums.
"""
class Solution:
    # 3/1072 passed
    def maximizeGreatness(self, nums: List[int]) -> int:
        res = 0
        perms = []
        def permute(i):
            nonlocal res
            perms.append(nums[:])
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                permute(i+1)                
                nums[i], nums[j] = nums[j], nums[i]
        permute(0)
        for perm in perms:
            greatness = 0
            for n, p in zip(nums, perm):
                if p > n:
                    greatness += 1
            res = max(res, greatness)
        return res
            
class Solution:
    # 1067 / 1072 test cases passed.
    def maximizeGreatness(self, nums: List[int]) -> int:
        # replace the number with the next larger number
        # if there is no next larget number, replace it with the smallest number
        sortedn = sorted(nums)
        used = [False for i in range(len(nums))]
        perm = []
        for n in nums:
            # print("n ", n)
            replace = False
            for i in range(len(nums)):
                if sortedn[i] > n and not used[i]:
                    perm.append(sortedn[i])
                    used[i] = True
                    replace = True
                    break
            if not replace:
                for i in range(len(nums)):
                    if not used[i]:
                        perm.append(sortedn[i])
                        used[i] = True
                        replace = True
                        break
        res = 0
        for n, p in zip(nums, perm):
            if p > n:
                res += 1
        return res

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        # Sort then start from index 0 to check how many pairs of nums[ans] < nums[j] we can have.
        nums.sort()
        res = 0
        for n in nums:
            if nums[res] < n:
                res += 1
        return res

            
        