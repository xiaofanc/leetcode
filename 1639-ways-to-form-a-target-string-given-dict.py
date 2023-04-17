"""
dp[i][k]: ways to form target[0:i] using word[0:k]
1. we do not use word[k] to form target[i]
dp[i][k] = dp[i][k-1]

2 we use word[k] to form target[i]
dp[i][k] += dp[i-1][k-1] * count(how many word[k] == target[i])

n = len(target), m = len(words[0])
return dp[n][m]

sol 2:
res[j] means the number of ways to form target j first characters.

"""

class Solution:
    def numWays(self, words, target):
        n, mod = len(target), 10**9 + 7
        res = [1] + [0] * n
        # print("res -->", res)
        for i in range(len(words[0])):
            # print("i", i)
            count = collections.Counter(w[i] for w in words)
            # print("count -->", count)
            for j in range(min(i, n - 1), -1, -1):
                # print("j: ", j)
                res[j + 1] += res[j] * count[target[j]] % mod
                # print("res: ", res)
        return res[n] % mod

class Solution:
    # TLE
    def numWays(self, words: List[str], target: str) -> int:    
        size = len(words[0])
        m = 10**9+7
        # number of ways to form target[i:] using words[..][j:]
        @cache
        def dp(i, j): 
            # base case: there is one way not to put any characters
            if i == len(target):
                return 1
            # base case: empty string cannot make target
            if j == size:
                return 0
            res = 0
            # count the occ of target[i] in words[..][j]
            # use column j
            cnt = 0
            for word in words:
                if word[j] == target[i]:
                    cnt += 1
            # for the current character, there is cnt ways
            res += cnt * dp(i+1, j+1)

            # skip column j
            res += dp(i, j+1)

            res = res % m
            return res
        return dp(0, 0)

class Solution:
    # bottom-up DP
    def numWays(self, words: List[str], target: str) -> int:    
        size = len(words[0])
        m = 10**9+7
        count = [[0] * 26 for _ in range(size)]
        # count number of chars in position j: O(nk)
        for word in words:
            for j in range(size):
                count[j][ord(word[j]) - ord('a')] += 1
        # number of ways to form target[i:] using words[..][j:]: O(mk)
        @cache
        def dp(i, j): 
            # base case: there is one way not to put any characters
            if i == len(target):
                return 1
            # base case: empty string cannot make target
            if j == size:
                return 0
            res = 0
            # count the occ of target[i] in words[..][j]
            # use column j
            # cnt = 0
            # for word in words:
            #     if word[j] == target[i]:
            #         cnt += 1
            cnt = count[j][ord(target[i]) - ord('a')]
            # for the current character, there is cnt ways
            res += cnt * dp(i+1, j+1)

            # skip column j
            res += dp(i, j+1)

            res = res % m
            return res
        return dp(0, 0)
                    
if __name__ == '__main__':
	s = Solution()
	print(s.numWays(["acca","bbbb","caca"], "aba"))  # 6


    