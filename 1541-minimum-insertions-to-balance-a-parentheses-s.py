class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))","]")
        # print(s)
        p = [] # store "("
        res = 0
        for c in s:
            if c == "(":
                p.append(c)
            elif (c == "]" or c == ")") and p:
                if c == ")":
                    res += 1
                    p.pop()
                else:
                    p.pop()
            elif (c == "]" or c == ")") and not p:
                if c == "]":
                    res += 1
                else:
                    res += 2
                
        return res + len(p)*2
 

     def minInsertions(self, s: str) -> int:
        right = 0 # store the needed ")"
        res = 0   # store the parentheses already added
        for c in s:
            if c == "(":
                # check previous situation
                if right % 2 == 1:
                    right -= 1
                    res += 1   # need one ")"
                right += 2 
            else:
                right -= 1
                if right < 0:
                    right += 2
                    res += 1   # need one "("
        return res + right

if __name__ == '__main__':
    s = Solution()
    print(s.minInsertions(")))))))"))   # 5                 
                    
                
                
                