class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)
    
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        def rev(w):
            l, r = 0, len(w)-1
            while l < r:
                w[l], w[r] = w[r], w[l]
                l += 1
                r -= 1
            return w
        
        for i in range(0, len(s), 2*k):
            s[i: i+k] = rev(s[i:i+k])
    
        return "".join(s)
            
if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefg", 2))