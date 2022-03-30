"""
KMP:
Example: 文本串：‘aabaab aafa’  模式串：‘aabaaf’
长度为前1个字符的子串a，最长相同前后缀的长度为0。
长度为前2个字符的子串aa，最长相同前后缀的长度为1。
长度为前3个字符的子串aab，最长相同前后缀的长度为0。
长度为前4个字符的子串aaba，最长相同前后缀的长度为1。
长度为前5个字符的子串aabaa，最长相同前后缀的长度为2。
长度为前6个字符的子串aabaaf，最长相同前后缀的长度为0。
前缀表： 0，1，0，1，2，0
找到的不匹配的位置， 那么此时我们要看它的前一个字符的前缀表的数值是多少。
为什么要前一个字符的前缀表的数值呢，因为要找前面字符串的最长相同的前缀和后缀。
所以要看前一位的 前缀表的数值。
前一个字符的前缀表的数值是2， 所有把下标移动到模式串下标2的位置继续比配. 'aa'已经匹配上了。

"""
class Solution:
    # def strStr0(self, haystack: str, needle: str) -> int:
    #     for i in range(len(haystack) - len(needle) + 1):
    #         if haystack[i:i+len(needle)] == needle[:]:
    #             return i
            
    #     return -1
        
    # def strStr1(self, haystack: str, needle: str) -> int:     
    #     return haystack.find(needle)
    
    # Time limit exceed
    def strStr2(self, haystack, needle): 
        nexttable = self.getNext(needle)
        print('nexttable', nexttable)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            while haystack[i] != needle[j]:
                # needle pointer returns back to the end of prefix 'b'
                j = nexttable[j-1]
                #print(i, j)
                continue
            else:
                i += 1
                j += 1
                #print(i, j)
        
        return i - j if j == len(needle) else -1

    # passed -> O(M+N)
    def strStr3(self, haystack, needle): 
        if len(needle) == 0:
            return 0
        nexttable = self.getNext(needle)
        print('nexttable', nexttable)
        j = 0
        for i in range(len(haystack)): # O(N)
            while j > 0 and haystack[i] != needle[j]:
                j = nexttable[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

    def getNext(self, t):
        # create prefix table -> O(M)
        nexttable = [0] * len(t)
        # j = end of prefix, i = end of postfix
        j = 0 
        for i in range(1, len(t)):
            while t[i] != t[j] and j > 0:
                # j return back
                j = nexttable[j-1]
            if t[i] == t[j]:
                j += 1
            nexttable[i] = j
        return nexttable

s=Solution()
# print(s.strStr0("hello","ll"))
# print(s.strStr1("hello","ll"))
print(s.strStr2("aabaabaaf","aabaaf"))
