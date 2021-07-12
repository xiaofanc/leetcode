from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # give the smallest child the smallest cookie which is >= the child's hungry degree
        children = sorted(g)
        cookie = sorted(s)
        i, j = 0, 0
        res = 0
        while i < len(children) and j < len(cookie):
            if cookie[j] >= children[i]:
                res += 1
                j += 1
                i += 1
            else:
                j += 1
        return res

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # give the smallest child the smallest cookie which is >= the child's hungry degree
        children = sorted(g)
        cookies = sorted(s)
        child, cookie = 0, 0
        while child < len(children) and cookie < len(cookies):
            if children[child] <= cookies[cookie]:
                child += 1
            cookie += 1
        return child

if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1,2,3], [1,1])) # 1
    print(s.findContentChildren([1,2], [1,2,3])) # 2




    