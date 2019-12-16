import collections

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = [float("-inf"), float("-inf"), float("-inf")]
        for v in nums:
            if v not in m:
                if   v > m[0]: m = [v, m[0], m[1]]
                elif v > m[1]: m = [m[0], v, m[1]]
                elif v > m[2]: m = [m[0], m[1], v]
        return m[0] if float("-inf") in m else m[2]
                
                    
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        counter = sorted(counter.items(), reverse=True)
        if len(counter) < 3:
            return counter[0][0]
        else:
            return counter[2][0]

if __name__ == '__main__':
    s = Solution()
    print(s.thirdMax([2,2,3,1]) == 1)