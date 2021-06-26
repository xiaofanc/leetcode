# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero. 

# The solution set must not contain duplicate triplets.

# 2 pointers

from typing import List
#a+b+c = 0
class Solution:
    def threeSum0(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        N = len(nums)
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, N - 1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0 :
                    r -= 1
                else:
                    res.append((nums[i],nums[l], nums[r]))
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r-=1;
        return res

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        #固定i，rangei的右边做two sum
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = set()
            for x in nums[i+1:]:
                if x not in d:
                    d.add(-v-x)
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))  # trasform to list


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i, v in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            d = set()
            # find target -v using 2 sum
            for x in nums[i+1:]:
                left = -v-x
                if left not in d:
                    d.add(x)
                else:
                    res.add((v, x, -v-x))
        return res
                    

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i, v in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l, r = l+1, r-1
        return res
 

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums.sort()
        #print(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, results)
        return results

    def twoSum(self, nums, i, res):
        lo, hi = i+1, len(nums)-1
        while lo < hi:
        s = nums[i] + nums[lo] + nums[hi]
        if s < 0:
            lo += 1
        elif s > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            #print(res)
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo-1]:
                lo += 1
                #print(lo)
            while lo < hi and nums[hi] == nums[hi+1]:
                hi -= 1
                #print(hi)

    def twoSum(self, nums, i, res):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i]-nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            seen.add(nums[j])
            j += 1  

# without sort
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1-val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement)))) # remove duplicates
                        # print('res', res)
                    seen[val2] = i
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum0([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum1([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum1([-1, 0, 1, 2, -1, -4]))
