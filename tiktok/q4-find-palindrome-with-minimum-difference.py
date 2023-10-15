"""
Q4. Find palindrome with minimum difference
https://stackoverflow.com/questions/77085260/find-palindrome-with-minimum-difference

Given an array of strings, each string has same length m.
The error between two strings s1 and s2 is defined as the sum of the absolute distance between the characters s1[i] and s2[i] in the English alphabet.
Find a lexicographically smallest palindromic string say alpha of length m, such that the sum of the errors between this alpha string and the array of strings is minimum.

array = ["aa","yy","mm"] -> mm

The key insight here, is that the optimal character at index i is the median of all characters found at that index, and at the mirrored index (so counting backwards from the end of the string).
"""

def solution(arr):
	n, m = len(arr), len(arr[0])
	res = []
	for i in range((m+1)//2):
		counter = [0]*26
		j = m-i-1
		for word in arr:
			counter[ord(word[i])-ord('a')] += 1
			counter[ord(word[j])-ord('a')] += 1
		# Get the median character based on these character frequencies
		# print(counter)
		median = -1
		count = 0
		while count < n:
			median += 1
			count += counter[median]
			print("median, count, n", median, count, n)
		res.append(chr(median + ord('a')))
	s = "".join(res)
	return s + s[::-1][m%2:]


arr = ["aa","yy","mm"] # mm
arr = ['aba', 'cbd']  # aba
print(solution(arr))




