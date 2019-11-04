class Solution:
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            print(h)
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            print(h)
            if num in h:
                return h[num],i
            else:
                h[target-num] = i



s=Solution()
#print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2,3,2,4,1], 3))
