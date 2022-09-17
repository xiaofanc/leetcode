class Solution(object):
    # TLE: 92 / 136 test cases passed.
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        def isPalindrome(w1, w2):
            w = w1+w2
            return w == w[::-1]
            
        for i in range(len(words)):
            for j in range(i):
                if isPalindrome(words[i], words[j]):
                    res.append((i,j))
                if isPalindrome(words[j], words[i]):
                    res.append((j,i))
        return res
    
    # 135 / 136 test cases passed.
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def allValidSuffixes(word):
            # find all "valid suffix" of a word if the remainder (prefix) of the word forms a palindrome - word is w2
            suffix = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    suffix.append(word[i+1:])
            return suffix
        
        def allValidPrefixes(word):
            prefix = []
            for i in range(len(word)-1,-1,-1):
                if word[i:] == word[i:][::-1]:
                    prefix.append(word[:i])
            return prefix
        
        res = []
        lookUp = {}
        for i, w in enumerate(words): # word is distinct
            lookUp[w] = i
        
        # Time: O(n*k^2)
        for i, w in enumerate(words):
            
            # case 1: check if the reverse of word in present
            if w[::-1] in lookUp and lookUp[w[::-1]] != i: # O(k^2)
                res.append((lookUp[w[::-1]], i))
            # case 2: for each prefix of word, check if prefix is a palindrome. If it is a palindrome, then reverse the remaining suffix and check if it is in the list
            suffix = allValidSuffixes(w) # O(k^2)
            # print("suffix", w, suffix)
            for reversedw1 in suffix:  # O(k)
                w1 = reversedw1[::-1]
                if w1 in lookUp:
                    res.append((lookUp[w1], i))
            # case 3: for each suffix of word, check if suffix is a palindrome. If it is a palindrome, then reverse the remaining prefix and check if it is in the list
            prefix = allValidPrefixes(w)
            # print("prefix", w, prefix)
            for reversedw2 in prefix:
                w2 = reversedw2[::-1]
                if w2 in lookUp:
                    res.append((i, lookUp[w2]))
            # print("res->", i, res)
        return res
                    

        
        