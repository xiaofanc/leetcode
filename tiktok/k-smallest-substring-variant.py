"""
There is a string input consisting of character '0' and '1' only and an integer k. Find a substring of string input such that:
-> The length of the substring == k
-> The number of '1' == n
-> It is lexicographically smallest/largest

"""

class Solution:
	# Time: O(L*K), space: O(K)
	def ksmallestsubstring(self, s, k, n):
		def subsGen(s, k, n):
			cntone = 0 
			for i in range(len(s)-k+1):
				subs = s[i:i+k]
				if i == 0:
					cntone = subs.count('1')
				elif subs[-1] == '1':
					cntone += 1

				if cntone == n:
					yield subs
				if subs[0] == '1':
					cntone -= 1

		m = M = s[:k]
		for subs in subsGen(s, k, n):
			# subs in subsGen has the same length k and n '1's
			m = min(m, subs)
			M = max(M, subs)
		return m, M

if __name__ == '__main__':
	s = Solution()
	print(s.ksmallestsubstring('101110', 3, 2))


