"""
Find the shortest distance between two words
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]
"""
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsMap = defaultdict(list)
        for i, v in enumerate(wordsDict):
            self.wordsMap[v].append(i)
                
    def shortest(self, word1: str, word2: str) -> int:
        pos1 = sorted(self.wordsMap[word1])
        pos2 = sorted(self.wordsMap[word2])
        minDist = float("inf")
        i, j = 0, 0
        while i < len(pos1) and j < len(pos2):
            minDist = min(minDist, abs(pos1[i]-pos2[j]))
            if pos1[i] < pos2[j]:
                i += 1
            else:
                j += 1
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
