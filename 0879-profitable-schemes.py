
class Solution:
	# TLE: 7 / 45 testcases passed
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # sum of subset >= minProfit & sum of group <= n
        res = []
        def subset(i, profits, members, comb):
            if members > n:
                return
            if profits >= minProfit and members <= n:
                res.append(comb[:])
            for j in range(i, len(profit)):
                subset(j+1, profits+profit[j], members+group[j], comb+[j])
        subset(0, 0, 0, [])
        # print("res ", res)
        return len(res)

	"""
	i: The index of the crime that we are considering currently.
	members: The total number of members we have in the current subset we have selected.
	profits: The total profit we have generated so far with the current subset we selected.
	One more observation that could help us reduce the number of states is that once the total profit exceeds minProfit, it doesn't matter what the actual profit is anymore because we only care about making at least minProfit. If the profit is at least minProfit, we will mark the current selection as a profitable scheme; otherwise, not. Therefore, the profit in the states can be stored as min(profit, minProfit) so that the possible values for profit always remains less than or equal tominProfit, which can potentially save us many states in the memoization.
	"""
	# Time complexity: O(N⋅M⋅K)
	# Here, N is the maximum number of criminals allowed in a scheme, M is the size of the list group, and K is the value of minProfit
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # sum of subset >= minProfit & sum of group <= n
        dp = {}
        def subset(i, profits, members, comb):
            # up until i, with current profits and members, number of subsets that meet the condition
            if (i, profits, members) in dp:
                return dp[(i, profits, members)]
            if i == len(profit):
                if profits >= minProfit:
                    return 1
                return 0 
            # not include crime[i]
            res = subset(i+1, profits, members, comb)                  
            # include crime[i]
            if members + group[i] <= n:
                # res += subset(i+1, profits+profit[i], members+group[i], comb+[i])
                res += subset(i+1, min(profits+profit[i], minProfit), members+group[i], comb+[i])
            res = res % (10**9+7)
            dp[(i, profits, members)] = res
            return res
        return subset(0, 0, 0, [])





