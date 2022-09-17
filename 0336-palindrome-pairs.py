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
        
        