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
        nums = set(nums)
        i = 0
        while True:
            if i not in nums:
                return i 
            i += 1

    def missingNumber2(self, nums):
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= n
            res ^= i
        return res


s=Solution()
print(s.missingNumber0([0]))
print(s.missingNumber0([0,1,2,3,4]))
print(s.missingNumber1([0]))
print(s.missingNumber2([0]))
print(s.missingNumber2([0,1,2,3,4]))
print(s.missingNumber2([0,2,3,4,5]))
