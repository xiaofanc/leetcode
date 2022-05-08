"""
convert word1 to word2
word1 = "", word2 = "abc", res = len(word2)
word1 = "abc", word2 = "", res = len(word1)
word1 = "", word2 = "", res = 0
	       i
word1 = "abc", 
word2 = "adc"
           j
if word1[i] == word2[j]:
    (i+1,j+1)
else:
insert (i, j+1)
delete (i+1, j)
replace (i+1, j+1)

solution: bottom up DP
dp[i][j] = convert word1[i:] to word2[j:]

    a b c
 a        3
 d        2
 c      0 1
    3 2 1 0
"""

class Solution:
	def editdistance(self, word1, word2):
		w, h, = len(word1)+1, len(word2)+1
		dp = [[float("inf")] * w for _ in range(h)]
		# print("dp->", dp)
		for i in range(h):
			dp[i][w-1] = h-1-i
		for j in range(w):
			dp[h-1][j] = w-1-j
		# print("dp->", dp)
		for i in range(h-2, -1, -1):
			for j in range(w-2, -1, -1):
				if word1[j] == word2[i]:
					dp[i][j] = dp[i+1][j+1]
				else:
					dp[i][j] = 1+ min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
		return dp[0][0]
		# print(dp)

if __name__ == '__main__':
	s = Solution()
	# print(s.editdistance("abc", "adc"))
	print(s.editdistance("horse", "ros"))











