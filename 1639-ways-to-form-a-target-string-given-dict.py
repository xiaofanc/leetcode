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
        print("res -->", res)
        for i in range(len(words[0])):
            print("i", i)
            count = collections.Counter(w[i] for w in words)
            print("count -->", count)
            for j in range(min(i, n - 1), -1, -1):
                print("j: ", j)
                res[j + 1] += res[j] * count[target[j]] % mod
                print("res: ", res)
        return res[n] % mod

if __name__ == '__main__':
	s = Solution()
	print(s.numWays(["acca","bbbb","caca"], "aba"))  # 6