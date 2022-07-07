"""
dp[i+1] = longest valid parentheses before the matching "("
store the result into the next position

s  = " ( ) ( ( ) ) "
       0 1 2 3 4 5 6
dp =   0 0 0 0 0 0 0
stack = [0]

i = 1
stack = []
dp =   0 0 2 0 0 0 0
dp[2] = dp[0] + 1-0+1 = 2

i = 2
stack = [2]

i = 3
stack = [2,3]

i = 4
stack = [2]
dp =   0 0 2 0 0 2 0
dp[5] = dp[3] + 4-3+1 = 2

i = 5
stack = []
dp =   0 0 2 0 0 2 6
dp[6] = dp[2] + 5-2+1 = 6
"""

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
                # dp[last] -> longest valid parentheses before the matching "("
                # i - last + 1 -> valid parentheses substring between ")" and the matching "("
                dp[i+1] = dp[last] + i - last + 1 
                print(dp)
        return max(dp)
                
                
if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses(")()())") == 4)
    print(s.longestValidParentheses("()(())") == 6)


