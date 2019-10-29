class Solution:
    def strStr0(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle[:]:
                return i
            
        return -1
        
    def strStr1(self, haystack: str, needle: str) -> int:     
        return haystack.find(needle)
    
    def strStr2(self, haystack: str, needle: str) -> int:    
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] != needle[j]:
                i = i - j + 1
                j = 0
                #print(i, j)
                continue
            else:
                i += 1
                j += 1
                #print(i, j)
        
        return i - j if j == len(needle) else -1
                
                
s=Solution()
print(s.strStr0("hello","ll"))
print(s.strStr1("hello","ll"))
print(s.strStr2("hello","ll"))
