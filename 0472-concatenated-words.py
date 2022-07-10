"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        
        def dfs(word):
            for i in range(1, len(word)):
            	# must be concatenated by at least 2 words
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in words and suffix in words:
                    return True
                if prefix in words and dfs(suffix):
                    return True
                if suffix in words and dfs(prefix):
                    return True
            return False
        
        for word in words:
            if dfs(word):
                res.append(word)
        return res


    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        res = []
        memo = {}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in words and suffix in words:
                    memo[word] = True
                    break
                if prefix in words and dfs(suffix):
                    memo[word] = True
                    break
                if suffix in words and dfs(prefix):
                    memo[word] = True
                    break
            return memo[word]
                    
        for word in words:
            if dfs(word):
                res.append(word)
        return res

if __name__ == '__main__':
	s = Solution()
	print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))  # ["catsdogcats","dogcatsdog","ratcatdogcat"]



