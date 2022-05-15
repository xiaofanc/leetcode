"""
The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND greater than 0.

"""

class Solution:
	# TLE
    def largestCombination(self, candidates: List[int]) -> int:
        
        def bitwise(comb):
            if comb:
                r = comb[0]
                for c in comb[1:]:
                    r = r & c
                return r
            return 0
        
        def combinations(i, comb, res):
            if bitwise(comb[:]) > 0 and len(comb) > res:
                res = len(comb)
            for j in range(i, len(candidates)):
                comb.append(candidates[j])
                res = combinations(j+1, comb, res)
                comb.pop()
            return res
        
        res = 0
        res = combinations(0, [], res)
        return res
            
if __name__ == '__main__':
	s = Solution()
	print(s.largestCombination([16,17,71,62,12,24,14])) # 4 (The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0)
	