"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
'a*' can be ["", "a", "aa", "aaa"...]

edge cases:
if p[j] is out of bound while s[i] is not, return False
if s[i] is out of bound while p[j] is not, not sure: "a" => "a*b*"

'aa'->'a*'
when p[j+1] == "*":
    if using '*' to delete previous chars, then compare (s[i:], p[j+2:])
    if using '*' to add chars, then first char must match & compare (s[i+1:], p[j:])
        - why first char must match? 'ba'->'a*' False, no b in pattern
        - why compare s[i+1:] and p[j:]?   'aaaab'->'a*b' since a might be repeated
else p[j+1] != "*":
    first_match & compare (s[i+1:], p[j+1:])

"""
def match(a,b):
    if a == "" and b == "":
        return True
    else:
        return a[0] == b[0] and match(a[1:], b[1:])


class Solution:
    # Time: O(M x N)
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

    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if j >= len(p) and i >= len(s):
                return True
            if j >= len(p):
                return False
            # i can be out of bound, "a" => "a*b*"
            # compare the current position
            match = (i < len(s) and (s[i] == p[j] or p[j] == "."))
            # check the next position
            if j+1 < len(p) and p[j+1] == "*":
                return (dfs(i, j+2) or # not use *
                match and dfs(i+1, j)) # use *
            else:
                return match and dfs(i+1, j+1)
            return False
        return dfs(0,0)

    # memorization
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            if j >= len(p) and i >= len(s):
                return True
            if j >= len(p):
                return False
            # when i == len(s), check if p[j:] can represent empty string
            # compare the current position
            match = (i < len(s) and (s[i] == p[j] or p[j] == "."))
            # check the next position
            if j+1 < len(p) and p[j+1] == "*":
                cache[(i,j)] = (dfs(i, j+2) or # not use *
                match and dfs(i+1, j)) # use *
                return cache[(i,j)]
            else:
                cache[(i,j)] = match and dfs(i+1, j+1)
                return cache[(i,j)]
            
            cache[(i,j)] = False
            return cache[(i,j)]

        return dfs(0,0)

    # DP
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

    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(s, i, p, j):
            # base case
            if j == len(p):
                return i == len(s)
            if i == len(s):
                # check if p[j:] can represent empty string
                # p[j:] must be in the format of a*b*c*
                if (len(p)-j) % 2 == 1:
                    return False
                for x in range(j+1, len(p), 2):
                    if p[x] != "*":
                        return False
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            # first match
            if s[i] == p[j] or p[j] == ".":
                # check if p[j+1] == "*"
                if j+1 < len(p) and p[j+1] == "*":
                    # delete or use p[j]
                    memo[(i, j)] = dp(s, i, p, j+2) or dp(s, i+1, p, j)
                    return memo[(i, j)]
                else:
                    # check next positions
                    memo[(i, j)] = dp(s, i+1, p, j+1)
                    return memo[(i, j)]
            else:
                if j+1 < len(p) and p[j+1] == "*":
                    # delete p[j]
                    memo[(i, j)] = dp(s, i, p, j+2)
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = False
                    return memo[(i, j)]
        return dp(s, 0, p, 0)

if __name__ == '__main__':
    print(match("abc","acb"))
    print(match("abc","abc"))

    s = Solution()
    print( (s.isMatch("aa", "a") == False))
    #Explanation: "a" does not match the entire string "aa".

    print( (s.isMatch("aa", "a*") == True))
    #Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' twice, it becomes "aa".

    print( (s.isMatch("ab", ".*") == True))
    #Explanation: ".*" means "zero or more (*) of any character (.)".

    print( (s.isMatch("aab", "c*a*b") == True))
    #Explanation: c can be repeated 0 times, a can be repeated 2 time. Therefore, it matches "aab".

    print( (s.isMatch("mississippi", "mis*is*p*.") == False))
