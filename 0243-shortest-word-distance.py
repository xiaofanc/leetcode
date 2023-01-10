"""
word1 and word2 are in wordsDict.
word1 != word2.
"""

from typing import List

class Solution:
    def shortestDistance0(self, words: List[str], word1: str, word2: str) -> int:
        min_dist = len(words)
        curr_word, idx = None, 0
        for i,w in enumerate(words):
            if w not in (word1, word2):
                continue
            if curr_word and w!= curr_word:
                min_dist= min(min_dist, i-idx)
            curr_word, idx = w, i
            print(w,i,min_dist)
        return min_dist

    def shortestDistance2(self, words: List[str], word1: str, word2: str) -> int:
        index1 = [i for i in range(len(words)) if words[i] == word1]
        index2 = [i for i in range(len(words)) if words[i] == word2]
        return min([abs(i-j) for i in index1 for j in index2])

    def shortestDistance3(self, words, word1, word2):
        p1 = p2 = float('inf')
        result = float('inf')
    
        for i, w in enumerate(words):
            if w == word1:
                p1 = i
            elif w == word2:
                p2 = i
            result = min(abs(p2 - p1), result)
                    
        return result

    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        prev = -1
        res = len(wordsDict)
        for i, w in enumerate(wordsDict):
            if w == word1 or w == word2:
                if prev != -1 and (w != wordsDict[prev]):
                    res = min(res, i-prev)
                prev = i
        return res
        
if __name__ == '__main__':
    s=s = Solution()
    print(s.shortestDistance0(["practice", "makes", "perfect", "coding", "makes"],"coding","practice")) # 3
    print(s.shortestDistance1(["practice", "makes", "perfect", "coding", "makes"],"coding","practice")) # 3
    print(s.shortestDistance2(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))
    print(s.shortestDistance3(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))


    