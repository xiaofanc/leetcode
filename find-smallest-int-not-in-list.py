

class Solution:
	def smallestposint(self, lists):
		lists = [x for x in lists if x > 0]
		lists = sorted(lists)
		print(lists)
		if not lists:
			return 1
		for i in range(1, len(lists)):
			print("lists[i]", lists[i])
			if lists[i] == lists[i-1]:
				continue
			if lists[i] != lists[i-1]+1:
				return lists[i-1]+1
		return lists[-1]+1


if __name__ == '__main__':
	s = Solution()
	print(s.smallestposint([1,3,6,4,1,2])) # 5
	print(s.smallestposint([-1,-2])) # 1
	print(s.smallestposint([1,2,3])) # 4