# stack

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
                stack.pop()  # stack must have values to pop
            else: # stack is empty
                return False
        return stack == [] #stack must be empty

s=Solution()
print(s.isValid("()[]{}"))
print(s.isValid("([))]{}"))
print(s.isValid("({()[]})"))
