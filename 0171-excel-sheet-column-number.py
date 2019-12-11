class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        ordA = ord("A")
        for c in s:
            ans = ans*26 + ord(c) - ordA + 1
        return ans
    
    def titleToNumber(self, s: str) -> int:
        return sum(26**i * (ord(c)-ord('A')+1) for i,c in enumerate(s[::-1]))

    def titleToNumber(self, s: str) -> int:
        n = len(s)-1
        return sum(26**(n-i)*(ord(c)-ord('A')+1) for i,c in enumerate(s))

    def titleToNumber(self, s: str) -> int:
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])

if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber("A"))  #1
    print(s.titleToNumber("AB")) #28
    print(s.titleToNumber("ZY")) #701 