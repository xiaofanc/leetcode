class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = [0]*26
        window = [0]*26
        for char in s1:
            target[ord(char)-ord('a')] += 1
        l, r = 0, 0
        while r < len(s2):
            # print("l, r->", l,r, window)
            window[ord(s2[r])-ord('a')] += 1
            # if window size is not == len(s1), move left pointer
            if r-l+1 > len(s1):
                window[ord(s2[l])-ord('a')] -= 1
                l += 1
            if window == target:
                return True
            r += 1
        return False
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A = [ord(x)-ord('a') for x in s1]
        B = [ord(y)-ord('a') for y in s2]
        
        target = [0]*26
        window = [0]*26
        for x in A:
            target[x] += 1
            
        for i, y in enumerate(B):
            window[y] += 1
            if i >= len(A):
                window[B[i-len(A)]] -= 1
            if window == target:
                return True
        return False

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        c1, c2 = Counter(s1), Counter(s2[:l1])
        i, j = 0, l1
        while j < l2:
            if c1 == c2:
                return True
            c2[s2[j]] += 1
            c2[s2[i]] -= 1
            if c2[s2[i]] == 0: c2.pop(s2[i])
            i += 1
            j += 1
            #print(c1, c2)
            #print()
        return c1 == c2
        
if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo")) #True
    print(s.checkInclusion("ab", "eidboaooo")) #False
    print(s.checkInclusion("adc", "dcda")) #True

