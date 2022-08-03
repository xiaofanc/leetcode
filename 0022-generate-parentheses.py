"""
We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left=0, right=0):
            # must have n left and right parenthesis
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            # left parenthesis cannot be more than n
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            # right parenthesis cannnot be more than left in the current combination
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
                
        backtrack([], 0, 0)
        return ans
                
if __name__ == '__main__':
	s = Solution()
	print(s.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]