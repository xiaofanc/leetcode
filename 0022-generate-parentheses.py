"""
We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.

The height of the tree is 2n, since we must branch once per bracket. So the number of vertices is at most 2^2n and the number of leaves is at most half the number of vertices of a perfect tree, so asymptotically O(2^2n). Additionally we do linear work per leaf to copy the sequence to output.

A more complete analysis would take into account that some bracket choices are invalid, which leads to asymptotically fewer leaves in the tree. However since we are interested in upper bounds, it's still correct to say that time complexity is O(n*(2^2n)), even though it's not the most accurate upper bound.
"""
class Solution:
    # Time: upper bound -> O(n*(2^2n))
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


    