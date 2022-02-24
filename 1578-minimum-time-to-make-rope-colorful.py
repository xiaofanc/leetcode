class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) <= 1:
            return 0
        slow, fast = 0, 1
        res = []
        while fast < len(colors):
            if colors[slow] == colors[fast]:
                fast += 1
                if fast == len(colors):
                    res.extend(self.removemin(slow, fast, neededTime[slow:fast]))
            else:
                if fast - slow > 1: # get same color ballons
                    # need to remove fast-1-slow ballons
                    res.extend(self.removemin(slow, fast, neededTime[slow:fast]))
                    slow = fast
                else:
                    slow += 1
                    fast += 1
        return sum(res)
            
    def removemin(self, slow, fast, neededTime):
        ballons = []
        neededTime.sort()
        for i in range(len(neededTime)):
            if len(ballons) < fast-1-slow:
                ballons.append(neededTime[i])
            else:
                break
        return ballons

"""
For each group of continuous same characters,
we need cost = sum_cost(group) - max_cost(group)
"""
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = colors[0]
        fee = local_sum = local_max = 0
        for cur, cur_cost in zip(colors, neededTime):
            if cur == prev:
                local_sum += cur_cost
                local_max = max(local_max, cur_cost)
            else:
                fee += local_sum - local_max
                local_sum, local_max = cur_cost, cur_cost
                prev = cur
        return fee + local_sum - local_max
        
if __name__ == '__main__':
    s = Solution()
    print(s.minCost("abaac", [1,2,3,4,5])) # 3
    print(s.minCost("aabaa", [1,2,3,4,1])) # 2


