class Solution(object):
    def wordPattern(self, pattern, word_str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = word_str.split(" ")
        if len(pattern) != len(words):
            return False

		# use two dictionaries, mapping character / string with index
        pattern_map, word_map = {}, {}
        for i in xrange(len(pattern)):
            # when character / string shows in the first time, return -1
            if pattern_map.get(pattern[i], -1) != word_map.get(words[i], -1):
                return False
            # when character / string shows in the first time, save the index
            pattern_map[pattern[i]] = word_map[words[i]] = i

        return True
      
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        t = str.split()
        s = pattern
        # return the first occurance of a string in string
        # return the first occurance of the element in a list
        return map(s.find, s) == map(t.index, t)

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        x = str.split()
        lsp = len(set(pattern))
        lsx = len(set(x))
        return len(pattern) == len(x) and lsp == lsx and lsp == len(set(zip(pattern, x)))



if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))        
    print(s.wordPattern("abba", "dog cat cat fish"))
    print(s.wordPattern("aaaa", "dog cat cat fish"))





