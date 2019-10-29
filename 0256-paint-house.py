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

s=Solution()
print(s.minCost0([[17,2,17],[16,16,5],[14,3,19]]))
#print(s.minCost1([[17,2,17],[16,16,5],[14,3,19]]))
#check reduce function