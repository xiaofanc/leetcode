
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for j in range(len(s)):
            for i in range(j+1):
                t = s[i:j+1]
                if set(t) == set(t.swapcase()):
                    ans = max(ans, t, key=len)
        return ans

    def longestNiceSubstring(self, s: str) -> str:
        bad = set(s) - set(s.swapcase())
        if not bad:
            return s
        # print("split->", s.split(bad.pop())) -> ["Ya", "aAay"] -> ["aAa"]
        return max(map(self.longestNiceSubstring, s.split(bad.pop())), key=len)

    def longestNiceSubstring(self, s: str) -> str: 
		"""
		build a set of all letters (e.g.: {a,A, y,Y,z})
		go through the string, check if it has an invalid letter (for which NOT both upper and lower case version are in the set)
		if so, split the string and check recursively for the left and the right substring if they are valid. return the longer one.
		"""
		if not s:
            return s
        ss = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in ss:
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key = len)
        return s

if __name__ == '__main__':
	s = Solution()
	print(s.longestNiceSubstring("YazaAay"))  # "aAa"




