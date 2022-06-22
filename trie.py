def Trie(words):
    word_key = "$"

    trie = {}
    for word in words:
        node = trie
        for letter in word:
            # if letter not in the dictionary, return default {}
            node = node.setdefault(letter, {})
        # mark the existence of a word in trie node
        node[word_key] = word
        print("node", node)
    print(trie)
    return trie

print(Trie(["a", "abc", "acf"]))

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


if __name__ == '__main__':
    t = Trie()
    t.insert("apple")
    print("trie", t.trie)
    print(t.search("app"))
    print(t.startsWith("app"))

    
