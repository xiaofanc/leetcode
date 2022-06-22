"""
Implement the WordDictionary class:

WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

"""

class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.word_key = "$"
    
    # Time: O(M), M - key length
    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node[self.word_key] = word
    
    # Time: O(M) for well-defined words, O(Nx26^M) for undefined words
    def search(self, word: str) -> bool:
        return self.searchInNode(word, self.trie)
                    
    def searchInNode(self, word, dct):
        node = dct
        for i in range(len(word)):
            char = word[i]
            if char not in node:
                # if char is '.', check all possible nodes at this level
                if char == '.':
                    for x in node:
                        if x != self.word_key and self.searchInNode(word[i+1:], node[x]):
                            return True
                # if char != '.':
                return False
            # if the char is found, go down to the next level
            else:
                node = node[char]
        return self.word_key in node
            
                
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)