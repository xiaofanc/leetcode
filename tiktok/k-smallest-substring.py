"""
There is a string input consisting of character '0' and '1' only and an integer k. Find a substring of string input such that:
-> The number of '1' == k
-> It has the smallest length
-> It is lexicographically smallest

"""
class Solution:
	# Time: O(N^2)
	def ksmallestsubstring(self, s, k):
		minlen = len(s)
		candidates = []
		for i in range(len(s)):
			numones = 0
			for j in range(i, len(s)):
				if s[j] == '1':
					numones += 1
					if numones == k:
						if j-i+1 <= minlen:
							minlen = min(minlen, j-i+1)
							candidates.append(s[i:j+1])
						break
		ans = '1' * len(s)
		for candidate in candidates:
			if len(candidate) == minlen:
				# print("candidate", candidate)
				if candidate < ans:
					ans = candidate
		return ans

	# Time: O(N)
	def ksmallestsubstring2(self, s, k):	
		arr = [] # store '1' index
		for i in range(len(s)):
			if s[i] == '1':
				arr.append(i)

		res = '1' * len(s)
		for i in range(len(arr)-k+1):
			subs = s[arr[i]:arr[i+k-1]+1]
			if len(subs) < len(res):
				res = subs
			elif len(subs) == len(res) and subs < res:
				res = subs
		return res

if __name__ == '__main__':
	s = Solution()
	print(s.ksmallestsubstring('0101101', 3)) # '1011'
	print(s.ksmallestsubstring2('0101101', 3)) # '1011'



