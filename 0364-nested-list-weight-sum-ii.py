# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    
        def findMaxDepth(lst):
            maxDepth = 1
            for nested in lst:
                if not nested.isInteger():
                    maxDepth = max(maxDepth, 1+findMaxDepth(nested.getList()))
            return maxDepth
        
        def weightedSum(lst, depth, maxDepth):
            res = 0
            for nested in lst:
                if nested.isInteger():
                    res += nested.getInteger() * (maxDepth-depth+1)                    
                else:
                    res += weightedSum(nested.getList(), depth+1, maxDepth)
            return res
        
        maxDepth = findMaxDepth(nestedList)
        return weightedSum(nestedList, 1, maxDepth)
        
if __name__ == '__main__':
    s = Solution()
    print(s.depthSumInverse([[1,1],2,[1,1]])) # 1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
    print(s.depthSumInverse([1,[4,[6]]])) # 1*3 + 4*2 + 6*1 = 17
    print(s.depthSumInverse([[1,1],2,[1,1],[[[[]]]]])) # 20 ?
    # maxDepth = 5
    # depth = 2 2 1 2 2 
    # weights = 4 4 5 4 4 
    # res = 4 + 4 + 10 + 4 + 4 = 26



    



