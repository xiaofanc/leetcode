class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            if len(s) % i == 0:
                pattern = s[:i] * (len(s)//i)
                if pattern == s:
                    return True
        return False

#The maximum length of a "repeated" substring that you could get from a string would be half it's length
#For example, s = "abcdabcd", "abcd" of len = 4, is the repeated substring.
#You cannot have a substring >(len(s)/2), that can be repeated.
#
#So, when ss = s + s , we will have atleast 4 parts of "repeated substring" in ss.
#(s+s)[1:-1], With this we are removing 1st char and last char => Out of 4 parts of repeated substring, 2 part will be gone (they will no longer have the same substring).
#ss.find(s) != -1, But still we have 2 parts out of which we can make s. And that's how ss should have s, if s has repeated substring.

    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        ss = (s+s)[1:-1]
        return ss.find(s) != -1
        # return s in (2*s)[1:-1]

"""
KMP:
如果len % (len - (prefix_table[len - 1])) == 0 ，则说明 (数组长度-最长相等前后缀的长度) 正好可以被数组的长度整除，说明有该字符串有重复的子字符串。
数组长度减去最长相同前后缀的长度相当于是第一个周期的长度，也就是一个周期的长度，如果这个周期可以被整除，就说明整个数组就是这个周期的循环。
https://programmercarl.com/0459.%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
"""

    def repeatedSubstringPattern2(self, s: str) -> bool:
        if not s:
            return False
        prefix_table = self.getNext(s)
        # len(s)-prefix_table[-1] -> 第一个周期的长度
        if prefix_table[-1] != 0 and len(s) % (len(s)-prefix_table[-1]) == 0:
            return True
        return False
    
    def getNext(self, s):
        j = 0
        # prefix_table[i]：当前位置最长相同前缀后缀长度
        prefix_table = [0] * len(s)
        for i in range(1, len(s)):
            while s[j] != s[i] and j > 0:
                j = prefix_table[j-1]
            if s[j] == s[i]:
                j += 1
            prefix_table[i] = j
        return prefix_table

if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern2("abab")) # True
    # prefix_table: [0,0,0,0,1,2,3,4,5,6,7,8] # 12 % (12-8) == 0
    print(s.repeatedSubstringPattern2("asdfasdfasdf")) # True




