class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # sort the given dictionary 
        # check if any of the words given in the dictionary is a subsequence of s
        dictionary.sort()
        res = ""
        for w in dictionary:
            for i in range(len(w)):
                j = 0 # pointer for s
                while i < len(w) and j < len(s):
                    # print(w, s, i, j)
                    if w[i] == s[j]:
                        i += 1
                        j += 1
                    else:
                        j += 1
                # if j reaches end
                # move to the next word
                if j == len(s):
                    break
            # check if i reaches end - word is a subsequence
            if i == len(w):
                if len(w) > len(res):
                    res = w
                    # print(res)
        return res

    def findLongestWord(self, S, D):
        D.sort(key = lambda x: (-len(x), x))
        for word in D:
            i = 0
            for c in S:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""
        
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def issubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        # return the string with the max length or lexicographically smallest
        return max(sorted(filter(issubsequence, dictionary)) + [''], key=len)

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def issubsequence(x):
            it = iter(s)
            return all(c in it for c in x)
        
        return min(list(filter(issubsequence, dictionary)) + [""], key=lambda x: (-len(x), x))

if __name__ == '__main__':
    s = Solution()
    print(s.findLongestWord("abpcplea", ["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"])) # apple


