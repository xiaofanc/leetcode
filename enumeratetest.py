class Solution(object):
	"""docstring for isenumerate"""
	def isnumerate(self,order):
		order_index = []
		for i, c in enumerate(order):
			order_index.append((i,c))
		return order_index
				
s=Solution()
print(s.isnumerate('dnncshd'))

		