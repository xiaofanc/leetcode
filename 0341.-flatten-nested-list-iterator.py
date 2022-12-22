# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._integers = []
        self._position = -1
        def flatten_list(nestedList):
            for nested_integers in nestedList:
                if nested_integers.isInteger():
                    self._integers.append(nested_integers.getInteger())
                else:
                    flatten_list(nested_integers.getList())
        flatten_list(nestedList)
    
    def next(self) -> int:
        self._position += 1
        return self._integers[self._position]
        
    
    def hasNext(self) -> bool:
        if self._position + 1 < len(self._integers):
            return True
        return False
         

class NestedIterator:
    """
    For this example:
    [1,[4,[6, 3], 5]] -> reverse
    [[4, [6, 3], 5], 1] -> pop 1
    [4, [6, 3], 5] -> [5, [6, 3], 4]
    [5, [6, 3], 4] -> pop 4
    [5, [6, 3]] -> pop [6, 3] -> [3, 6] -> [5, 3, 6]
    [5, 3, 6] -> pop 6
    [5, 3] -> pop 3
    [5] -> pop 5
    """
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))       
    
    def next(self) -> int:
        # self.makestacktopinteger()
        return self.stack.pop().getInteger()
           
    def hasNext(self) -> bool:
        self.makestacktopinteger()
        return len(self.stack) > 0
     
    def makestacktopinteger(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop().getList()))

# generator
class NestedIterator:
    # Time: O(1)
    def __init__(self, nestedList: [NestedInteger]):
        self.generator = self._generator(nestedList)
        self.peek = None # next element

    def _generator(self, nestedList):
        for nestedint in nestedList:
            if nestedint.isInteger():
                yield nestedint.getInteger()
            else:
                yield from self._generator(nestedint.getList())

    # Time: O(1)
    def next(self) -> int:
        next_int, self.peek = self.peek, None
        return next_int

    # Time: O((N+L)/N)
    def hasNext(self) -> bool:
        if self.peek != None:
            return True
        try:
            self.peek = next(self.generator)  
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())




