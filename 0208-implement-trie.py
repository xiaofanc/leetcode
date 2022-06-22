
class Trie:

    def __init__(self):
        self.trie = {}
        self.word_key = "$"

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
        	# node = node.setdefault(char, {})
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.word_key] = word
        
    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        if self.word_key in node and node[self.word_key] == word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        # make sure prefix exists, no need to check the word
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

    # def startsWith(self, prefix: str) -> bool:
    #     node = self.trie
    #     for char in prefix:
    #         if char not in node:
    #             return False
    #         node = node[char]
    #     stack = [[k, v] for k, v in node.items()]
    #     while stack:
    #         k, v = stack.pop()
    #         if k == self.word_key:
    #             return True
    #         else:
    #             for a, b in v.items():
    #                 stack.append([a, b])
    #     return False
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)