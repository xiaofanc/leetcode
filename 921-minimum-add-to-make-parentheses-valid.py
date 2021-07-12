class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")" and stack:
                stack.pop()
            else:
                res += 1
        return len(stack) + res

    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        left = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")" and left == 0:
                count += 1 
            else:
                left -= 1
        return count + left
        
if __name__ == '__main__':
    s = Solution()
    print(s.minAddToMakeValid("())"))  # 1
    print(s.minAddToMakeValid("()))((")  # 4
    print(s.minAddToMakeValid("(((")  # 3
