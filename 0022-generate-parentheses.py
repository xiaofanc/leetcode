"""
We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left=0, right=0):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
                
        backtrack([], 0, 0)
        return ans
                
if __name__ == '__main__':
	s = Solution()
	print(s.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]