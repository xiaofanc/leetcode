"""
2390.
You are given a string s, which contains stars *.

In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
"""

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*' and stack:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
                