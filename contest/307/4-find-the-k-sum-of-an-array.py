
class Solution:
    # TLE: 13 / 111 test cases passed.
    def kSum(self, nums: List[int], k: int) -> int:
        res = [0]
        for n in nums:
            temp = res[:]
            for i in range(len(temp)):
                s = temp[i]
                idx = bisect.bisect_left(res, n+s)
                res.insert(idx, n+s)
                
        # res.sort(reverse=True)
        # print("res->", res)
        return res[-k]