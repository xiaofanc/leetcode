"""
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
"""
class Solution(object):
	"""docstring for Solution"""
	def ishappy(self, n):
		seen = set()
		while n not in seen:
			seen.add(n)
			n = sum([int(i)**2 for i in str(n)])
		return n == 1


s=Solution()
print(s.ishappy(44232))
print(s.ishappy(332784))
print(s.ishappy(38854))
print(s.ishappy(98351))
print(s.ishappy(70918))
print(s.ishappy(53112))

		
		