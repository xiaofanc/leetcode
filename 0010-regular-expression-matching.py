def match(a,b):
    if a == "" and b == "":
        return True
    else:
        return a[0] == b[0] and match(a[1:], b[1:])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""
        first_match = (s != "" and (p[0] == s[0] or p[0] == "."))
        # zero or more (*)
        if len(p) >= 2 and p[1] == "*":
            return (self.isMatch(s, p[2:]) or 
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    #memorization
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        lens, lenp = len(s), len(p)
        # dp(i, j) = match(s[i:], p[j:])
        def dp(si, pi):
            if (si, pi) in memo:
                return memo[(si, pi)]
            if pi == lenp:
                ans = (si == lens)
            else:
                first_match = (si < lens) and p[pi] in set([s[si], "."])
                if pi <= lenp-2 and p[pi+1] == "*":
                    ans = dp(si, pi+2) or (first_match and dp(si+1, pi))
                else:
                    ans = first_match and dp(si+1, pi+1)
            memo[(si, pi)] = ans
            return ans
        return dp(0,0)

    #DP
    def isMatch(self, s: str, p: str) -> bool:
        lens, lenp = len(s), len(p)
        dp = [[False]*(lenp+1) for _ in range(lens+1)]
        dp[-1][-1] = True # base case: "" == ""
        for si in range(lens, -1, -1): 
            for pi in range(lenp-1, -1, -1):
                first_match = (si<lens) and p[pi] in {s[si], "."}
                if pi <= lenp-2 and p[pi+1] == "*":
                    dp[si][pi] = dp[si][pi+2] or (first_match and dp[si+1][pi])
                else:
                    dp[si][pi] = first_match and dp[si+1][pi+1]
        return dp[0][0]

if __name__ == '__main__':
    print(match("abc","acb"))
    print(match("abc","abc"))

    s = Solution()
    print( (s.isMatch("aa", "a") == False))
    #Explanation: "a" does not match the entire string "aa".

    print( (s.isMatch("aa", "a*") == True))
    #Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

    print( (s.isMatch("ab", ".*") == True))
    #Explanation: ".*" means "zero or more (*) of any character (.)".

    print( (s.isMatch("aab", "c*a*b") == True))
    #Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

    print( (s.isMatch("mississippi", "mis*is*p*.") == False))
