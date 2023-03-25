"""
You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].
"""
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        for i, char in enumerate(str(format(n, 'b'))[::-1]):
            if i % 2 == 0:
                even += int(char)
            else:
                odd += int(char)
        return [even, odd]
            