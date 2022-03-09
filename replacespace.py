
class Solution:
	def replacespace(self, s, target):
		count = s.count(" ")
		res = list(s)
		res.extend([" "] * count * (len(target)-1))
		print(res)
		l, r = len(s)-1, len(res)-1
		while l < r:
			if res[l] == " ":
				res[r-len(target)+1: r+1] = target
				r = r-len(target)
			else:
				res[r] = res[l]
				r -= 1
			l -= 1

		return ''.join(res)

if __name__ == '__main__':
	s = Solution()
	print(s.replacespace("We are happy.", "%20"))
