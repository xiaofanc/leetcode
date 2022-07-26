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
        
s=Solution()
print(s.minCost0([[17,2,17],[16,16,5],[14,3,19]]))
#print(s.minCost1([[17,2,17],[16,16,5],[14,3,19]]))
#check reduce function