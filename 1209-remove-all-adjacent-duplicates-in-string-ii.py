class Solution:

    # time limit exceed
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if len(stack) >= k-1 and c == stack[-1]:
                # print("stack: ", stack)
                # print("stack[1-k: ]", stack[1-k: ])
                if len(set(stack[1-k:])) == 1:
                    stack = stack[:len(stack)-(k-1)]
                    # print("stack: ", stack)
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return "".join(stack)

    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or c != stack[-1][0]:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
            
            if stack[-1][1] == k:
                stack.pop()
        
        return ''.join([a[0]*a[1] for a in stack])

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates("iiiixxxxxiiccccczzffffflllllllllfffffllyyyyyuuuuuz", 5)) # "izzlz"




    