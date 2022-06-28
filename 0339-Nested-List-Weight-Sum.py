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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth, ret = 1, 0
        while nestedList:
            ret += depth*sum([x.getInteger() for x in nestedList if x.isInteger()])
            nestedList = sum([x.getList() for x in nestedList if not x.isInteger()],[])
            # c = [[1,2],[5,9],[4]]
            # sum(c,[]) = [1, 2, 5, 9, 4]
            depth += 1
        return ret
        
    #iterate
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        if len(nestedList) == 0:
            return 0
        stack = []
        sum = 0
        for n in nestedList:
            stack.append((n,1))          # first append the first level
        while stack:
            next, d = stack.pop(0)
            if next.isInteger():         # check if first element in the first level is integer
                sum += d*next.getInteger()
            else:                        # if it is not integer, append list to stack with depth + 1
                for i in next.getList():
                    stack.append((i, d+1))
        return sum 

    # DFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def dfs(lst, depth):
            res = 0
            for nested in lst:
                if nested.isInteger():
                    res += nested.getInteger() * depth
                else:
                    res += dfs(nested.getList(), depth+1)
            return res
        
        return dfs(nestedList, 1)
        
