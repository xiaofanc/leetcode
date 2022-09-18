"""
You are given an array words of size n consisting of non-empty strings.

We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.

Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
Explanation: The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.
"""

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        def findAllPrefix(word):
            prefixes = []
            for i in range(len(word)):
                prefix = word[:i+1]
                prefixes.append(prefix)
            return prefixes
        
        dct = defaultdict(int)
        for word in words:
            for p in findAllPrefix(word):
                dct[p] = dct.get(p, 0) + 1
        
        ans = [0]*len(words)
        for i, word in enumerate(words):
            for p in findAllPrefix(word):
                ans[i] += dct[p]
        return ans


        