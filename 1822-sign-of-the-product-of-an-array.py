class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for n in nums:
            prod *= n
        if prod > 0: return 1
        elif prod < 0: return -1
        return 0
        # return 0 if not prod else 1 if prod > 0 else -1

    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                sign = -sign
        return sign
        
if __name__ == '__main__':
    s = Solution()
    print(s.arraySign(-1,-2,-3)) # -1