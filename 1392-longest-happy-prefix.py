"""
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

rooling hash:
eg. ABC
Prefix - A * 128 ^ 2 + B * 128 ^ 1 + C
Suffix - C + B * 128 ^ 1 + A * 128 ^ 2

https://leetcode.com/problems/longest-happy-prefix/discuss/547237/JavaPython-Rolling-Hash
https://leetcode.com/problems/longest-happy-prefix/discuss/551533/Python-Rolling-Hash-Explanation-of-Lee215's-solution
"""

class Solution:
	# Time limit exceed
    def longestPrefix(self, s: str) -> str:
        # prefix = []
        # suffix = []
        for i in range(1, len(s)):
            p = s[::-1][i:][::-1]
            t = s[i:]
            # prefix.append(p)
            # suffix.append(t)
            if p == t:
                return p
        # print(prefix) -> ['leve', 'lev', 'le', 'l']
        # print(suffix) -> ['evel', 'vel', 'el', 'l']
        # for i in range(len(prefix)):
        #     if prefix[i] == suffix[i]:
        #         return prefix[i]
        return ""

# The basic idea is to calculate a hash for both the prefix and suffix and check if the two agree.

    def longestPrefix(self, s):
        # res stores the index of the end of the prefix, used for output the result
        # l stores the hash key for prefix
        # r stores the hash key for suffix
        # mod is used to make sure that the hash value doesn't get too big, you can choose another mod value if you want.
        res, l, r, mod = 0, 0, 0, 10**9 + 7

        # now we start from the beginning and the end of the string
        # note you shouldn't search the whole string! because the longest prefix and suffix is the string itself
        for i in range(len(s) - 1):

            # based on an idea that is similar to prefix sum, we calculate the prefix hash in O(1) time.
            # specifically, we multiply the current prefix by 128 (which is the length of ASCII, but you can use another value as well)
            # then add in the ASCII value of the upcoming letter
            l = (l * 128 + ord(s[i])) % mod

            # similarly, we can calculate the suffix hash in O(1) time.
            # Specifically, we get the ith letter from the end using s[~i], note ~i is -i-1
            # we find the pow(128, i, mod) and multiply by the letter's ASCII value
            # Actually, if we don't care about the beautifulness of the code, you can have a variable to keep track of pow(128, i, mod) as you increase i
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod

           # we check if the prefix and suffix agrees, if yes, we find yet another longer prefix, so we record the index
            if l == r: res = i + 1

       # after we finish searching the string, output the prefix
        return s[:res]
if __name__ == '__main__':
	s = Solution()
	print(s.longestPrefix("level")) # "l"

