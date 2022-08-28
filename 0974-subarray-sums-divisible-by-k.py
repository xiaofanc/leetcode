class Solution:
    # TLE
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s % k == 0:
                    res += 1
        return res

    # if sum(nums[:j]) % k = d and sum(nums[:i]) % k == d
    # then sum_i = n*k+d, sum_j = m*k+d
    # so sum_i-sum_j = (n-m)*k
    # so we only need to store subsum % k as the key, count how many prefix sum has the same mod
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sumMod = {0:1} # Mod:count
        s = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            m = s % k
            # print("sumMod->", sumMod)
            if m in sumMod:
                res += sumMod[m]
            sumMod[m] = sumMod.get(m, 0) + 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.subarraysDivByK([4,5,0,-2,-3,1], k=5)) 