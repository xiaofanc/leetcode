import re

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ""
        else:
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            if str1[:len(str2)] == str2:
                return self.gcdOfStrings(str1[len(str2):], str2)
            else:
                return ""

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ""

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # the smallest common factor
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)
        d = gcd(len(str1), len(str2))

        return str1[:d] if str1[:d] * (len(str2)//d) == str2 and str2[:d] * (len(str1)//d) == str1 else ""

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # the smallest common factor
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)
        d = gcd(len(str1), len(str2))
        gcd_str = str1[:d]
        ptn = '(' + gcd_str + ')+'
        return gcd_str if re.fullmatch(ptn, str1) and re.fullmatch(ptn, str2) else ""

if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings("ABABAB","ABAB"))









