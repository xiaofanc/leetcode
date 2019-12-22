from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2
        return i == len(bits) - 1 # if out of bound, then 2-bit char

if __name__ == '__main__':
	s = Solution()
	print(s.isOneBitCharacter([0,0,1,0,1,1,1,0,0,0,0]))