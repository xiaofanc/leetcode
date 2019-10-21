class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jset = set(J)
        return sum(s in jset for s in S)

s=Solution()
print(s.numJewelsInStones("aA","aAAbbbb"))