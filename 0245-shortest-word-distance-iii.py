"""
word1 and word2 are in the list and they represent two individual words in the list (could be the same).
"""
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        iMap = defaultdict(list)
        for i, word in enumerate(wordsDict):
            iMap[word].append(i)
        dist = len(wordsDict)
        l1, l2 = iMap[word1], iMap[word2]
        if word1 == word2:
            for i in range(len(l1)-1):
                dist = min(dist, l1[i+1]-l1[i])
        else:        
            i, j = 0, 0
            while i < len(l1) and j < len(l2):
                dist = min(dist, abs(l1[i]-l2[j]))
                if l1[i] > l2[j]:
                    j += 1
                else:
                    i += 1
        return dist

if __name__ == '__main__':
	s = Solution()
	print(s.shortestWordDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"))