from typing import List
from functools import reduce
import collections

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda c: (-len(c), c))
        #print(words)
        wordset = set(words)
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word
        
        return ""
            
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda c: len(c))
        #print(words)
        filtered = set([""])
        for word in words:
            if word[:-1] in filtered:
                filtered.add(word)
        #print(filtered)
        return max(sorted(filtered), key=lambda w:len(w)) # key = len


    def longestWord(self, words: List[str]) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True
        
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i
        
        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])
                
        return ans

if __name__ == '__main__':
	s = Solution()
	print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple")