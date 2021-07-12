class Solution:

    # time: O(n), space: O(1)
    def maxDepth(self, s: str) -> int:
        
        cur = 0 # store how many parenthesis left
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                cur += 1
                res = max(res, cur)
            if s[i] == ")":
                cur -= 1
        if cur == 0:
            return res
        return 0

    # time: O(n), space: O(n)
    def maxDepth(self, s: str) -> int:
        p = []
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                p.append(s[i])
            if s[i] == ")":
                if len(p) > res:
                    res = len(p)
                p.pop()
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth("8*((1*(5+6))*(8/6))")) # 3
    print(s.maxDepth("(1)+((2))+(((3)))")) # 3





    
