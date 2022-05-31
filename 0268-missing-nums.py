class Solution(object):
    def missingNumber0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = max(nums)
        uniq = set(i for i in range(n+1))
        for i in nums:
            if i in uniq:
                uniq.remove(i)
        uniq = list(uniq)
        if len(uniq) == 0:
            return n+1
        return uniq[0]
        
    def missingNumber1(self, nums):
        nums = set(nums) # O(N)
        i = 0
        while True:
            if i not in nums:
                return i 
            i += 1

    # XOR: (exclusive or) different -> 1, same -> 0
    # 2 (10) ^ 3 (11) = 0 1
    # 5 ^ 5 = 0
    # 5 ^ 5 ^ 3 = 3
    def missingNumber2(self, nums):
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= n
            res ^= i
        return res

    # sum([0,1,2,3]) - sum([0,1,3])
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res

s=Solution()
print(s.missingNumber0([0]))
print(s.missingNumber0([0,1,2,3,4]))
print(s.missingNumber1([0]))
print(s.missingNumber2([0]))
print(s.missingNumber2([0,1,2,3,4]))
print(s.missingNumber2([0,2,3,4,5]))
