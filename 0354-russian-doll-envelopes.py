
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 按w生序排序，如果w相同，按h降序排序
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        height = [1]*len(envelopes)

        def lengthOfLIS(nums):
            if not nums:
                return 0
            seq = []
            for num in nums:
                i = bisect_left(seq, num)
                if i == len(seq):
                    seq.append(num)
                else:
                    seq[i] = num
            return len(seq)

        for i in range(len(envelopes)):
            height[i] = envelopes[i][1]

        return lengthOfLIS(height)


class Solution:
    # 85 / 87 testcases passed
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        height = [1]*len(envelopes)
        dp = [1]*len(envelopes)

        def lengthOfLIS(nums):
            # find the longest increasing subsequence ends with i
            if not nums:
                return 0
            for i in range(len(nums)):
                for j in range(i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i], dp[j]+1)
            return max(dp)
            
        for i in range(len(envelopes)):
            height[i] = envelopes[i][1]

        return lengthOfLIS(height)
        
