class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        res = ""
        while a < len(word1) and b < len(word2):
            res += word1[a]
            a += 1
            res += word2[b]
            b += 1
        
        if a < len(word1):
            res += word1[a:]

        if b < len(word2):
            res += word2[b:]
        return res

