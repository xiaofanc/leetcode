"""
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
"""

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1, 100):
            if n*i % 2 == 0:
                return n*i
                
            