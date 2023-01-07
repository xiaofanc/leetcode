from typing import List
from functools import reduce
class Solution:
    def minCost0(self, costs: List[List[int]]) -> int:
        prev = [0] * 3
        for now in costs:
            prev = [now[i] + min(prev[:i] + prev[i+1:]) for i in range(3)]
        return min(prev)

    #def minCost1(self, costs):
    #    return min(reduce(lambda(A,B,C), (a,b,c): (a+min(B,C), b+min(A,C), c+min(A,B)),
    #                  costs, [0]*3))

    # bottom-up: O(n); top-down is fine too.
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(len(costs)-2,-1,-1):
            for j in range(3):
                if j == 0:
                    costs[i][0] += min(costs[i+1][1], costs[i+1][2])
                elif j == 1:
                    costs[i][1] += min(costs[i+1][0], costs[i+1][2])
                else:
                    costs[i][2] += min(costs[i+1][0], costs[i+1][1])
        return min(costs[0])

    # top-down: O(n) with memoization; O(2^n) without memoization
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}
        def paintCost(n, color):
            # total cost to paint the n house with this color
            if (n, color) in memo:
                return memo[(n, color)]
            cost = costs[n][color]
            if n == len(costs)-1:
                memo[(n, color)] = cost
                return cost
            elif color == 0:
                cost += min(paintCost(n+1, 1), paintCost(n+1, 2))
            elif color == 1:
                cost += min(paintCost(n+1, 0), paintCost(n+1, 2))
            else:
                cost += min(paintCost(n+1, 0), paintCost(n+1, 1))
            memo[(n, color)] = cost
            return cost
        
        if costs == []: return 0
        return min(paintCost(0,0), paintCost(0,1), paintCost(0,2))

s=Solution()
print(s.minCost0([[17,2,17],[16,16,5],[14,3,19]]))
#print(s.minCost1([[17,2,17],[16,16,5],[14,3,19]]))



