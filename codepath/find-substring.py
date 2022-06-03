"""
solution: two pointers
Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.
"""
class solution:
	def findsubstring(self, s1, s2):
		m, n = len(s1), len(s2)
		if n > m:
			return False
		l, r = 0, 0
		while l < m and r < n:
			if s1[l] == s2[r]:
				l += 1
				r += 1
			else:
				r = 0
				if s1[l] != s2[r]:
					l += 1
			# print("l, r", l, r)
		if n == 0 or r == n:
			return True
		return False

if __name__ == '__main__':
	s = solution()
	print(s.findsubstring("abcde", "cd"))   # True
	print(s.findsubstring("abccdd", "cd"))  # True
	print(s.findsubstring("abccecd", "cd"))  # True
	print(s.findsubstring("abced", "cd"))   # False
		
