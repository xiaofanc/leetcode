#import bisect
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #class Wrap:
        #    def __getitem__(self, i):
        #        return isBadVersion(i)
        #return bisect.bisect(Wrap(), False, 0, n)
        left, right = 0, n-1
        while left <= right:
            mid = left+(right-left)//2
            if isBadVersion(mid) is True:
                right =  mid - 1
            else:
                left = mid + 1
        return left
    
    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.search(n)
    
    def search(self, n):
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    s = Solution()
    data = [0,0,1,1,1]
    isBadVersion = lambda n: data[n]
    print(s.firstBadVersion(len(data)))
        
