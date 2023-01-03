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

        # maxDepth = 1
        # def findMaxDepth(lst, depth):
        #     nonlocal maxDepth
        #     for nested in lst:
        #         if not nested.isInteger():
        #             if len(nested.getList()) == 0:
        #                 continue
        #             maxDepth = max(maxDepth, depth+1)
        #             findMaxDepth(nested.getList(), depth+1)
        # findMaxDepth(nestedList, 1)
         
        def findMaxDepth(lst):
            maxDepth = 1
            for nested in lst:
                if not nested.isInteger():
                    # Let maxDepth be the maximum depth of any integer, empty [] does not count
                    if len(nested.getList()) == 0: 
                        continue
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

    # single-pass DFS
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # (maxDepth + 1) * sumOfElements - sumOfProducts (a*depth)
        sumOfElements, sumOfProducts, maxd = 0, 0, 1
        def helper(nestedList, depth):
            nonlocal sumOfElements, sumOfProducts, maxd
            for element in nestedList:
                if element.isInteger():
                    sumOfElements += element.getInteger()
                    sumOfProducts += element.getInteger() * depth
                else:
                    if len(element.getList()) == 0:
                        continue
                    maxd = max(maxd, depth+1)
                    helper(element.getList(), depth+1)
        helper(nestedList, 1)
        return (maxd+1) * sumOfElements - sumOfProducts

    # single-pass BFS
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # (maxDepth + 1) * sumOfElements - sumOfProducts (a*depth)
        sumOfElements, sumOfProducts, d = 0, 0, 1
        queue = deque()
        for element in nestedList:
            queue.append(element)
        while queue:
            size = len(queue)
            for i in range(size):
                element = queue.popleft()
                if element.isInteger():
                    sumOfElements += element.getInteger()
                    sumOfProducts += element.getInteger() * d
                else:
                    if len(element.getList()) == 0:
                        continue
                    for next_element in element.getList():
                        queue.append(next_element)
            d += 1

        return d * sumOfElements - sumOfProducts

if __name__ == '__main__':
    s = Solution()
    print(s.depthSumInverse([[1,1],2,[1,1]])) # 1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
    print(s.depthSumInverse([1,[4,[6]]])) # 1*3 + 4*2 + 6*1 = 17
    # one failed case
    print(s.depthSumInverse([[1,1],2,[1,1],[[[[]]]]])) # expected - 20 ?
    # maxDepth = 5 -> 4, empty [] does not count
    # depth = 2 2 1 2 2 
    # weights = 4 4 5 4 4 -> 3 3 4 3 3 
    # res = 4 + 4 + 10 + 4 + 4 = 26 -> 20

"""
@jolee888 the maxDepth is 4 in this case. I know it is confusing. I got 26 at first as well. So I guess the problem mean to say "Let maxDepth be the maximum depth of any NestedInteger. " Instead of "Let maxDepth be the maximum depth of any integer."

the depth of [[[ [] ]]] itself is 3, not 4 since we shouldn't count the innermost [] as that is empty, or doesn't have a NestedInteger.
"""

    



