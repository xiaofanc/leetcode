class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        for a, b in zip(heights, sorted(heights)):
            if a != b:
                ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.heightChecker([1,1,4,2,1,3]) == 3)