import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #dic = {}
        #for item in s:
        #dic[item] = dic.get(item, 0) + 1
        counter = collections.Counter(s)
        count = 0
        for i, c in counter.items():
            if c % 2 == 1:
                count += 1
        return True if count <= 1 else False
        # return sum(v % 2 for v in collections.Counter(s).values()) < 2
            
if __name__ == '__main__':
    s = Solution()
    print(s.canPermutePalindrome("aab") == True)
    print(s.canPermutePalindrome("code") == False)
    print(s.canPermutePalindrome("carerac") == True)