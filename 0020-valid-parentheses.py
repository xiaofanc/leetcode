class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        dct = {"(": ")", "[": "]",  "{": "}"}
        stack = []
        for i in range(len(s)):
            if s[i] in dct:
                stack.append(s[i])
            elif stack and s[i] == dct[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

s=Solution()
print(s.isValid("()[]{}"))
print(s.isValid("([))]{}"))
print(s.isValid("({()[]})"))
