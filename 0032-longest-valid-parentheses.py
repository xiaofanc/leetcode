class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lens = len(s)
        dp = [0]*(lens+1)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")" and stack:
                last = stack.pop()
                # dp - longest substring between ")" and the matching "("
                # dp[last] - the last substring
                dp[i+1] = dp[last] + i - last + 1 
                print(dp)
        return max(dp)
                
                
if __name__ == '__main__':
    s = Solution()
    print(s.(")()())") == 4)
    print(s.("()(())") == 6)