class Solution:
    # Time: O(log3N)
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 == 0:
                n = n/3
            else:
                return False
        return n == 1
            

    def isPowerOfThree(self, n: int) -> bool:
        # max value for the power of 3 is 3^19
        return n > 0 and 1162261467 % n == 0
        