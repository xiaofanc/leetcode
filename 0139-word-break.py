"""
let dp[i] = s[:i] can be built from wordDict
# dp[i]         = True if s[0:i] in wordDict
#               = True if dp[k] == True and s[k+1:i] in wordDict for 0<k<i
#               = False if no such k exist

base case:
dp[0] = True -> empty string can be built 
recusive rule:
when dp[i] = True?
dp[j] = True and s[j:i] in wordDict & j = [0,i-1]

"catsandog"
["cats", "dog", "sand", "and", "cat"]
[Ture, False, False, Ture(cat is in wordDict), True(cats is in wordDict), 
False(cats is in wordDict, but a is not in wordDict, and catsa is not in wordDict),
False, True(cats is in wordDict, and "and" is in wordDict), False, 
False(cats is in wordDict(True), but "andog" is not in wordDict)
     (catsand is in wordDict(True), but "og" is not in wordDict)]

"catsanddog"
DP[10]:
DP[0] + s[0:10]: True + "catsanddog" not in wordDict
DP[1] + s[1:10]: False + "atsanddog" not in wordDict
...
DP[4] + s[4:10]: ("cats")True + "anddog" not in wordDict
...
DP[7] + s[7:10]: ("catsand")True + "dog" in wordDict -> True

=> DP[7] true since DP[4] + ["and"] in wordDict

Time: O(N*M*N)
Space: O(N)

"""
def memo(f):
    m = dict()
    def wrapper(*args):
        if args not in m:  # list is not hashable
            m[args] = f(*args)
        return m[args]
    return wrapper


class Solution:
    # let dp[i] = s[:i] can be built from wordDict
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False]*len(s)
        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))
        return dp[-1]
    
    # Time: O(n^3) 
    # There are two nested loops, and substring computation at each iteration       
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        size = len(s)+1
        dp = [False] * size    # one more for empty string
        dp[0] = True
        for i in range(1, size):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break      # jump out of the j-loop
        return dp[size-1] 

    # Time: O(n^3) 
    # Size of recursion tree can go up to O(n^2) 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @memo
        def wordBreakMemo(s, wordDict, start):
            if start == len(s): # empty s
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and wordBreakMemo(s, wordDict, end):
                    return True
            return False
        
        return wordBreakMemo(s, frozenset(wordDict), 0) # frozenset is hashable, list is not

    # dp[i] = s[i:] can be built from the dict
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        # base case: s[8:] is empty
        dp[-1] = True  
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                # "leetcode"
                # dp[0] = s[:4] in dict & dp[4] == True
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True represents s[i:] is in the wordDict
        # dp[i] = True when there exists a j such that s[i:j] in the wordDict and dp[j] = True
        DP = [False] * (len(s)+1)
        DP[-1] = True
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)+1):
                if s[i:j] in wordDict and DP[j]:
                    DP[i] = True
        return DP[0]

    # Time: O(n * m^2), space: O(m^2)
    # no memo: Time: O(n^m * m)
    def wordBreak(self, s: str, wordDict: List[str], memo = {}) -> bool:
        if s in memo:
            return memo[s]
        if s == "":
            return True
        for word in wordDict:
            if s.find(word) == 0:          # find the word in s, return 0
                substring = s[len(word):]  # O(m)
                if self.wordBreak(substring, wordDict, memo):
                    memo[s] = True
                    return True
        memo[s] = False
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]) == True)




    