"""
LC 2055
Given a string s consisting of stars "*" and bars "|", an array of starting indices startIndex and an array of ending indices endIndex, determine the number of stars between any two bars within the substring between the two indices, inclusive, note that in this problem, indexing starts at 1.

s = '|**|*|*'
startIndex = [1,1]
endIndex = [5,6]

For the first pair of indices [1,5], the substring is '|**|*', there are 2 stars between a pair of bars.
For the second pait of indices [1,6], the substring is '|**|*|', there are 2+1=3 stars between bars.
return [2,3]

"""

class Solution:
	# Time: O(NK), space: O(NK)
	def starsAndBars(self, s, startIndex, endIndex):
		res = []
		for x, y in zip(startIndex, endIndex):
			substring = s[x-1:y]
			print('substring', substring)
			stack = []
			countbar = 0
			ans = 0
			for char in substring:
				if char == "|":
					if countbar:
						while stack:
							c = stack.pop()
							if c == "*":
								ans += 1
							else:
								countbar -= 1
					stack.append("|")
					countbar += 1
				elif char == "*" and countbar:
					stack.append('*')
			res.append(ans)
		return res

	# method 2 doesn't work
	def starsAndBars2(self, s, startIndex, endIndex):
		n =len(s)
		presum = [0]*n
		right = [0]*n
		left = [n]*n
		result = []

		count = 0
		for i in range(n):
			if s[i] == '*':
				count += 1
			presum[i] = count
		print('presum:', presum)

		temp = -1
		for i in range(n):
			if s[i] == "|":
				temp = i
			right[i] = temp 
		print('right:', right)

		temp = n 
		for i in range(n-1, -1, -1):
			if s[i] == "|":
				temp = i 
			left[i] = temp 
		print('left:', left)

		for query in zip(startIndex, endIndex):
			a = query[0]
			b = query[1]
			x = left[a]
			y = right[b]
			if x < y and x >= a and y <= b:
				result.append(presum[y]-presum[x])
			else:
				result.append(0)
		return result

if __name__ == '__main__':
	s = Solution()
	print(s.starsAndBars('|**|*|*', [1,1], [5,6])) # [2,3]
	print(s.starsAndBars('|**||*|*', [1,1], [5,6])) # [2,2]
	print(s.starsAndBars('**||*|*', [1,1], [5,6])) # [0,1]
	print(s.starsAndBars('**|**||*', [1,1], [5,6])) # [0,2]
	print(s.starsAndBars('|*||*|', [1,1], [5,6])) # [1,2]
	print(s.starsAndBars('*|*|', [1], [3])) # [0]





