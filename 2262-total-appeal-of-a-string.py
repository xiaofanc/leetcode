"""
It makes sense because we know that we just need to increment the number of current candidates that does not have duplicate characters that we are looking at i.

https://leetcode.com/problems/total-appeal-of-a-string/discuss/1996300/Python3-or-O(N)-O(1)-or-detail-for-beginners

828.
"""
class Solution:
	# TLE
    def appealSum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            unique = set()
            for j in range(i, len(s)):
                if s[j] not in unique:
                    unique.add(s[j])
                res += len(unique)
        return res

    def appealSum(self, s: str) -> int:
        res = 0
        lastSeenMap = {}
        prev, cur = 0, 0
        for i in range(len(s)):
            if s[i] not in lastSeenMap:
                cur = prev + (i+1)
            else:
                cur = prev + (i-lastSeenMap[s[i]])
            res += cur
            prev = cur
            lastSeenMap[s[i]] = i
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.appealSum("abbca")) # 28

