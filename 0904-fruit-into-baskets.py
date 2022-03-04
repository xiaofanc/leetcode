# find the longest subtring with only 2 numbers in it

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        basket = dict()
        maxlen = 0
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r],0) + 1
            if not basket or len(basket) <= 2:
                maxlen = max(maxlen, r-l+1)
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
                
        return maxlen

    def totalFruit(self, tree):
        count, i = {}, 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
        return j - i + 1
                        
if __name__ == '__main__':
	s = Solution()
	print(s.totalFruit([1,2,3,2,2]))  # 4