class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s = 0
        for i, cost in enumerate(costs):
            s += cost
            if s > coins:
                # print(i, s)
                return i
        return i+1

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        freq = [0]*(m+1) # i = cost
        cnt = 0
        # count sort
        for cost in costs:
            freq[cost] += 1

        for cost in range(1, m+1):
            if coins < cost:
                break
            # buy ice creams with current cost
            buy = min(freq[cost], coins//cost)
            coins -= cost*buy
            cnt += buy
        return cnt
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxIceCream([1,3,2,4,1], 7)) # 4
    print(s.maxIceCream([1,6,3,1,2,5], 20)) # 6

            