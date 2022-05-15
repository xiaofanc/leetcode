"""
The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND greater than 0.

If 'n' numbers ANDs up with each other to result in a number > 0, then there must be at least one bit set to True for all the 'n' numbers.
Reason: This is how AND works. If anyone of the bit is 0, then the whole AND result for that particular bit is zero.
An integer has at most 32 bits.

Approach:
Iterate through 32 places in the bits, check if candidate has 1 in the i place.
Return the max count of ones considering each bit for all the numbers.

Let’s understand from example only :

{16, 17, 71, 62, 12, 24, 14}

If we write the binary representations of these numbers -

16 → 0 0 1 0 0 0 0
17 → 0 0 1 0 0 0 1
71 → 1 0 0 0 1 1 1
62 → 0 1 1 1 1 1 0
12 → 0 0 0 1 1 0 0
24 → 0 0 1 1 0 0 0
14 → 0 0 0 1 1 1 0

Sum → 1 1 4 4 4 3 2

Ex. Sum[2] = 4, numbers → [16, 17, 62, 24]
Sum[3] = 4, numbers → [62, 12, 24, 14]
"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        # check max number of 1 in the 32 places
        for i in range(32):
            # x << y Returns x with the bits shifted to the left by y places
            # base case 1 in the i place
            x = 1 << i 
            count = 0
            # check how many numbers has 1 in the i place
            for j in range(len(candidates)):
                if candidates[j] & x == 0:
                    continue
                count += 1
            ans = max(ans, count)
        return ans

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
	