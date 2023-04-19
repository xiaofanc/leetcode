"""
Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

The concatenation of num1 and num2 is a permutation of num.
In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.

"""

class Solution:
    def splitNum(self, num: int) -> int:
        n1, n2 = 0, 0
        i = 0
        digits = []
        while num > 0:
            num, r = num // 10, num % 10
            digits.append(r)
        digits.sort()
        while i < len(digits):
            n1 = 10 * n1 + digits[i]
            i += 1
            if i < len(digits):
                n2 = 10 * n2 + digits[i]
                i += 1
        return n1+n2
        