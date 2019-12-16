class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            a = t.find(i)
            if a == -1:
                return False
            else:
                t = t[a+1:]
        return True
    
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)

    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

if __name__ == '__main__':
	s = Solution()
	print(s.isSubsequence("abc","ahbgdc"))            
                    
                    
        