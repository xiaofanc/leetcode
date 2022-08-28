"""
2391.
"""

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        M, P, G = 0, 0, 0 # get the last house for the truck
        cost = 0
        for i in range(len(garbage)-1,-1,-1):
            if not P and 'P' in garbage[i]:
                P = i
            if not M and 'M' in garbage[i]:
                M = i
            if not G and 'G' in garbage[i]:
                G = i
            if P and M and G:
                break

        cost += garbage[0].count('M')
        for i in range(1, M+1):
            cost += garbage[i].count('M') + travel[i-1]
            
        cost += garbage[0].count('P')
        for i in range(1, P+1):
            cost += garbage[i].count('P') + travel[i-1]
            
        cost += garbage[0].count('G')
        for i in range(1, G+1):
            cost += garbage[i].count('G') + travel[i-1]     
            
        return cost
