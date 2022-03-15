"""
LC 1621.
"""

class Solution:
    def numberOfSets(self, n, k):
        # same as given n + k - 1 points, take k segments, not allowed to share endpoints.
        # choose 2k points from n+k-1 and then group them in pairs to make segments.
        return math.comb(n + k - 1, k * 2) % (10**9 + 7)
    
if __name__ == '__main__':
	s = Solution()
	print(s.numberOfSets(4,2)) # 5