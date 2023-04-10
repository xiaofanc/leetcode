
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        idxes = defaultdict(list)
        for i, n in enumerate(nums):
            idxes[n].append(i)
        arr = [0]*len(nums)
        
        for k, vs in idxes.items():
            n = len(vs)
            if n == 1:
                continue
            totals = sum(vs)
            presum = 0
            for i, v in enumerate(vs): # [0,2,3]
                # arr[v] = sum(vs[i+1:]) - v*(n-i-1) - sum(vs[:i]) + v*i
                arr[v] = (totals - presum - v) - v*(n-i-1) + v*i - presum
                # = sum_r[nums[i]] - cnt_r[nums[i]] * i + cnt_l[nums[i]] * i - sum_l[nums[i]]
                # totals - 2 * presum + v * (2i - n)
                presum += v
        return arr
            
            
    def distance(self, nums: List[int]) -> List[int]:
        sum_l, sum_r, cnt_l, cnt_r = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        arr = [0] * len(nums)
        # left to right
        for i in range(len(nums)):
            # calculate sum of difference |i-j| for the left part
            # cnt_l -> number of indexes with same value as nums[i] on the left
            # sum_l -> sum of indexes with same value on the left
            arr[i] = cnt_l[nums[i]] * i - sum_l[nums[i]]
            sum_l[nums[i]] += i
            cnt_l[nums[i]] += 1
        # right to left
        for i in range(len(nums)-1,-1,-1):
            # calculate sum of difference |i-j| for the right part
            # cnt_r -> number of indexes with same value as nums[i] on the right
            # sum_r -> sum of indexes with same value on the right
            arr[i] += sum_r[nums[i]] - cnt_r[nums[i]] * i
            sum_r[nums[i]] += i
            cnt_r[nums[i]] += 1
        return arr




        