class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False]*len(s)
        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(i))
        return dp[-1]
           
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        size = len(s)+1
        dp = [False] * size
        dp[0] = True
        for i in range(1, size):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[size-1] 
        
if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]) == True)