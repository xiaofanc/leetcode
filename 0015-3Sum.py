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



if __name__ == '__main__':
    s = Solution()
    print(s.threeSum0([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum1([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum1([-1, 0, 1, 2, -1, -4]))
