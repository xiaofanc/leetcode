

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive int
            while y:
                x, y = x^y, (x&y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x^y, ((~x)&y) << 1
        
        return x * sign

# JAVA
"""
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}
"""