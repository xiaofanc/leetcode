import re

class Solution:
    def isPalindrome(self, s: str):
        cleaned = [c.lower() for c in s if c.isalpha() or c in '1234567890']
        return cleaned == cleaned[::-1]

    def isPalindrome(self, s: str):
        cleaned = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        return cleaned == cleaned[::-1]

    def isPalindrome(self, s: str):
        def gen(seq):
            for c in seq:
                if c.isalpha() or c.isdigit():
                    yield c.lower()
        return all(f==b for f,b in zip(gen(s), gen(reversed(s))))

    def isPalindrome(self, s: str):
        s = re.sub(r'\W+','',s).lower()
        return s == s[::-1]

    # space: O(1)
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].upper() == s[r].upper():
                    l += 1
                    r -= 1
                else:
                    return False
            # if s[l] is not alnum, move to the right and do not move outbound
            while not s[l].isalnum() and l < len(s)-1:
                l += 1
            # if s[r] is not alnum, move to the left and do not move outbound
            while not s[r].isalnum() and r > 0:
                r -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("0P") == False
    assert s.isPalindrome(";.") == True
    assert s.isPalindrome(".;;a......a'") == True


