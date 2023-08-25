class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        r = ""
        for w in words:
            r += w[0]
        return r == s
        