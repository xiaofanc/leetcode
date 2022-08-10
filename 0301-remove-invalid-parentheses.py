"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Input: s = "()())()"
Output: ["(())()","()()()"]
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # calculate how many left/right to remove
        left = 0
        right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0: # right is extra
                    right += 1
                if left > 0:  # find a matching )
                    left -= 1

        res = set()
        
        def recurse(index, left, right, expr, lrem, rrem):
            # left, right to keep track of how many left/right parentheses in the expr
            if index == len(s):
                if lrem == 0 and rrem == 0:
                    ans = "".join(expr)
                    res.add(ans)
            else:                
                if s[index] != "(" and s[index] != ")":
                    expr.append(s[index])
                    recurse(index+1, left, right, expr, lrem, rrem)
                    expr.pop()  # ?
                else:
                    # skip the current parenthesis
                    recurse(index+1, left, right, expr, lrem-(s[index] == "("), rrem-(s[index] == ")"))
                    # not skip the current index
                    expr.append(s[index])
                    if s[index] == "(":
                        recurse(index+1, left+1, right, expr, lrem, rrem)
                    elif s[index] == ")" and left > right:
                        recurse(index+1, left, right+1, expr, lrem, rrem)
                    expr.pop()
                    
        recurse(0, 0, 0, [], left, right)
        return res
    
