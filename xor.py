# XOR: Exclusive or, binary operation, same -> 0, difference -> 1
# 268. missing number
# [0,1,2,3] ^ [0,1,3] = 2

    def missingNumber(self, nums):
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= n
            res ^= i
        return res