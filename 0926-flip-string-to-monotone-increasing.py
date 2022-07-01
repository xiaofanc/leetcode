"""
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

"""
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # user prefix sum
        # p[i] means # ones for s[:i]
        p = [0]
        for i in range(len(s)):
            p.append(p[-1] + int(s[i]))
        res = float("inf")
        # if we want x zeros in the beginning and n-x ones in the end
        for x in range(len(s)+1):
            # number of ones needs to flip to zeros in the beginning = p[x]
            n1 = p[x]        
            # number of zeros needs to flip to ones in the latter = n-x - (p[-1]-p[x])
            n2 = (len(s)-x)-(p[-1]-p[x])
            res = min(res, n1+n2)
        return res
            
    def minFlipsMonoIncr(self, s: str) -> int:
        # calculate minflip for each position i if we want s[:i+1] all 0 and s[i+2:] all 1 
        n = len(s)
        ones = 0
        zeros = s.count('0')
        # edge case: flipping only zeros in the middle of the array: 11011
        minflip = zeros   
        for i in range(n):
        	# number of ones to be flipped to 0 in the beginning
            if s[i] == '1':
                ones += 1
            # number of zeros to be flipped to 1 in the end
            else:
                zeros -= 1
            
            minflip = min(minflip, ones+zeros)
        return minflip

if __name__ == '__main__':
	s = Solution()
	print(s.minFlipsMonoIncr("010110")) # 2
	print(s.minFlipsMonoIncr("11011")) # 1
