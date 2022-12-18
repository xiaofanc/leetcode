class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if set(words[i]) == set(words[j]):
                    res += 1
        return res
                    