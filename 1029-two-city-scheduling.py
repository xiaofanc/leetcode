class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # costA - costB to get the cost difference, sort by this
        # send the first n to A, and the last n to B
        costs.sort(key = lambda x: x[0]-x[1])
        total = 0
        n = len(costs) // 2
        for i in range(n):
            total += costs[i][0] + costs[i+n][1]
        return total

        # return sum(i[0] for i in costs[:len(costs)//2]) + sum(j[1] for j in costs[len(costs)//2:])

if __name__ == '__main__':
    s = Solution()
    print(s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))