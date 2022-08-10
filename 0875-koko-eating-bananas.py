class Solution:
    # TLE - O(mn)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 0
        total = float('inf')
        while total > h:
            speed += 1
            total = 0
            for p in piles:
                total += ceil(p/speed)
        return speed

"""
If Koko can eat all the piles with a speed of n, she can also finish the task with the speed of n+1. With a larger eating speed, Koko will spend less or equal time on every pile. Thus, the overall time is guaranteed to be less than or equal to that of the speed nn.
If Koko can't finish with a speed of n, then she can't finish with the speed of n - 1 either. With a smaller eating speed, Koko will spend more or equal time on every pile, thus the overall time will be greater than or equal to that of the speed n.
Binary search for the minimum value.
"""

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max speed = max(piles), then total time = len(piles), since h >= len(piles), then speed < max(piles)
        l, r = 1, max(piles)
        while l <= r:
            total = 0
            m = l + (r-l)//2
            for p in piles:
                total += ceil(p/m)
            if total > h: # too slow
                l = m + 1
            elif total <= h: # too fast
                r = m - 1
        return l   

if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed([30,11,23,4,20], 5)) # 30


    
