class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        cnt = [0]*len(nums) # store the count of the LIS ends with nums[i]
        length = [0]*len(nums) # store the longest increasing subseq ends with nums[i]
        maxL = float('-inf')
        res = 0
        for i in range(len(nums)):
            length[i] = cnt[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j]+1:
                        cnt[i] += cnt[j]
                    elif length[i] < length[j]+1:
                        length[i] = length[j]+1
                        cnt[i] = cnt[j]
            if maxL < length[i]:
                maxL = length[i]
                res = cnt[i]
            elif maxL == length[i]:
                res += cnt[i]
        return res
                    
if __name__ == '__main__':
    s = Solution()
    print(s.findNumberOfLIS([2,2,2,2,2])) # 5