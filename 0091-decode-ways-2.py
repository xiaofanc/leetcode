"""
dp[i] = number of ways to decode s[i:]
decode 0123: 0

decode 12345:
subproblems: 1+decode(2345), 12+decode(345)

decode 2345: 2+decode(“345”), 23+decode(“45”)
decode 2789: 2+decode(“789”)

decode 3678:
subproblems: 3+decode(678)

base case: dp[len(s)] = 1
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            elif s[i] == "1":
                dp[i] = dp[i+1]
                if i < len(s)-1:
                    dp[i] += dp[i+2]
            elif s[i] == "2":
                dp[i] = dp[i+1]
                if i < len(s)-1 and s[i+1] <= '6':
                    dp[i] += dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0] 

    def numDecodings(self, s: str) -> int:
        dp = {len(s):1} # base case
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            # if s[i:i+2] is in 10-26
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res
            return res
        return dfs(0)

    def numDecodings(self, s: str) -> int:
        dp = {len(s):1} # base case
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0": # "0123"
                dp[i] = 0
            else: # decode("323") = decode("23")
                dp[i] = dp[i+1]
            # if s[i:i+2] is in 10-26
            # decode("123") = decode("23") + decode("3")
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        return dp[0]

if __name__ == '__main__':
	s = Solution()
	print(s.numDecodings("1"))  # = decode("")
	print(s.numDecodings("12")) # = decode("2") + decode("")
	print(s.numDecodings("32")) # = decode("2")
	print(s.numDecodings("324")) # = decode("24")
	print(s.numDecodings("234")) # = decode("34") + decode("4")
	print(s.numDecodings("0234")) # 0
	print(s.numDecodings("2034")) # = decode("034") + decode("34") = 0 + 1 = 1




