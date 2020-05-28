"""
let dp[i] = s[:i] can be built from wordDict
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
DP[7] + s[7:10]: ("catsand")True + "dog" in wordDict -> True

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False]*len(s)
        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))
        return dp[-1]
           
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
        
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]) == True)