import collections
from functools import reduce
class Solution(object):
    def commonChars0(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = set(A[0].lower())
        for i in range(1,len(A)):
            res &= set(A[i])
        return list(res)
         
    def commonChars1(self, A):
        res = collections.Counter(A[0])
        for i in A:
            res &= collections.Counter(i)
        return list(res.elements()) # print each element
        
    def commonChars2(self, A):
        return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())

s=Solution()
print(s.commonChars0(["bella","label","roller"]))
print(s.commonChars1(["bella","label","roller"]))
print(s.commonChars2(["bella","label","roller"]))