class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opens = [], 0 
        for s in S:
            if s == "(" and opens > 0: res.append("(")
            if s == ")" and opens > 1: res.append(")")
            opens += 1 if s == "(" else -1
        return "".join(res)
    
    def removeOuterParentheses(self, S: str) -> str:
        parts = []
        left_n = 0
        right_n = 0

        # [j+1:i] will be slice getting parts without beginning and end
        j = 0  

        for i in range(len(S)):
            if S[i] == "(":
                left_n += 1  # add 1 when left parenthesis
            else:
                right_n += 1  # add 1 when right

            if left_n == right_n:
                parts.append(S[j + 1:i])  # add part when left_n = right_n
                j = i + 1  # because next first item will be cut, i + 1 gives j += 2 total
        return "".join(parts)

if __name__ == '__main__':
    s = Solution()
    print(s.removeOuterParentheses("(()())(())") == "()()()")
    print(s.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())")