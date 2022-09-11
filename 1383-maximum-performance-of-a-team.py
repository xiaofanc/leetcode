"""
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 10^9 + 7.

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
"""

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # find the fastest k-1 candidates with the fixed min efficiency
        # sort the candidates by efficiency in descending order
        candidates = sorted(zip(efficiency, speed), key=lambda x: -x[0])
        res = 0
        speedSum = 0
        h = []
        # select k-1 fastest candidates while treating i as the min effi
        for i, pair in enumerate(candidates):
            # efficiency: 9,7,5,4,3,2
            # speed"      1,5,2,10,3,8
            # fixed min efficiency from the current candidates
            # then select k-1 candidates with fastest speed from previous
            minE = pair[0]
            if len(h) > k-1: # must include current candidate
                top = heapq.heappop(h)
                speedSum -= top
            heapq.heappush(h, pair[1])
            speedSum += pair[1]
            # find the maximum performance for every fixed efficiency -> global
            res = max(res, speedSum*minE)
        return res % (10**9+7)
            
            
if __name__ == '__main__':
    s = Solution()
    print(s.maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2)) #60

    
