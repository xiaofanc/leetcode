class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []      
        for ch in S:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
                
        return ''.join(output)


    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack: 
                stack.append(c)
            else:
                if c == stack[-1]: 
                    stack.pop()
                else:
                    stack.append(c)
        return "".join(stack)
        
s = Solution()
print(s.removeDuplicates("abbaca"))