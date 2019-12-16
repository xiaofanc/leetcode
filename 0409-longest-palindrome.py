import collections
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        print(counter)
        sum = 0
        odd = 0
        for cnt in counter.values():
            if cnt % 2 == 0:
                sum += cnt
            else:
                odd = cnt % 2
                sum += cnt // 2 * 2  # add the even number of odd count
        if sum % 2 == 0 and odd == 1: # odd count exists
            sum += 1
        return sum

    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1: # add only once since ans will not be even again
                ans += 1
        #has_one = any(v for v in collections.Counter(s).values() if v%2 == 1)
        return ans

    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        res = sum(v // 2 * 2 for v in c.values())
        has_one = any(v for v in c.values() if v % 2 == 1)
        res += has_one
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abccccdd") == 7)
    print(s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth") == 983)