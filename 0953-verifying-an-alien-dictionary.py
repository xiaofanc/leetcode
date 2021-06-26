from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for idx, letter in enumerate(order):
            order_map[letter] = idx
        
        for i in range(len(words)-1):
            # compare words[i] and words[i+1] by each letter
            # print(i)
            for j in range(len(words[i])):
                # print(j)
                # if there is no difference between words[i] and words[i+1]
                # and the length of words[i] > words[i+1]
                if j >= len(words[i+1]):
                    return False
                if words[i][j] == words[i+1][j]:
                    continue
                else:
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False
                    # if we find the first difference and they are sorted
                    # no need to check the remaining letters
                    # check the next words
                    break
                

        return True
            

if __name__ == '__main__':
    s = Solution()
    print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
    print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
