"""
[1,1]
[10,8]
roads = [[6,4,9,7,1],[5,2,2,1,3],[3,2,5,5,2]]	
return 10?
= (1,1)->(3,2)->(5,5)->(6,4)->(9,7)->(10,8)
roads can be repeatly used or randomly used.
"""

class Solution:
    def minimumCost(self, start: List[int], target: List[int], roads: List[List[int]]) -> int:
        # store the least cost to reach (x,y)
        dct = {}

        def dfs(i, j, cost, d):
            # print(" "*d, "i, j ", i, j)
            nonlocal res
            if cost >= res:
                return
            res = min(res, cost+abs(target[0]-i)+abs(target[1]-j))
            # pruning
            if (i,j) in dct:
                if dct[(i,j)] <= cost:
                    return
            dct[(i,j)] = cost

            # use the special road
            for k in range(len(roads)):
                x1, y1, x2, y2, c = roads[k]
                dfs(x2, y2, cost+abs(x1-i)+abs(y1-j)+c, d+1)

        res = float('inf')
        dfs(start[0], start[1], 0, 0)
        return res
                   
            
                
            
            
