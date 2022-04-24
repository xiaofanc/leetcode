"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. 

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

methodology:
- create a decision tree by choosing 0 or 1 for each node
- if the path is not in nums, then return

other solution:
- start from '00', add 1 each time, then check if in nums
- at most check N+1 times

Time: worst case O(2^N) -> O(N^2)
Space: O(N)
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        res = []
        
        def backtrack(start, comb):
            if start == n:
                if comb not in nums:
                    res.append(comb[:])
                    return True
            for j in range(start, n):
                comb += '0'
                if backtrack(start+1, comb):
                    return res
                comb = comb[:-1]
                
                comb += '1'
                if backtrack(start+1, comb):
                    return res
                comb = comb[:-1]
        return backtrack(0, '')[0]

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        
        def backtrack(start, comb):
            if start == n:
                res = "".join(comb)
                return None if res in nums else res
            
            res = backtrack(start+1, comb)
            if res: return res
            
            comb[start] = "1"
            res = backtrack(start+1, comb)
            if res: return res
                
        return backtrack(0, ["0" for s in nums])

if __name__ == '__main__':
	s = Solution()
	print(s.findDifferentBinaryString(["01","10"]))  # '11'


