# if self.stream is a normal list -> time limit exceeded

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {} # store reversed word
        self.stream = []
        for word in words:
            node = self.trie
            for ch in word[::-1]:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter: str) -> bool:
        # search from the end of the stream and check char by char in trie
        self.stream.append(letter)
        node = self.trie
        # print("self.trie->", self.trie)
        for char in self.stream[::-1]:
            # print("char->", char)
            if "$" in node:
                return True
            if char not in node:
                return False
            node = node[char]
        return "$" in node
                
            
from collections import deque
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {} # store reversed word
        self.stream = deque()
        for word in words: # Time: O(M*N)
            node = self.trie
            for ch in word[::-1]:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter: str) -> bool:
        # search from the end of the stream and check char by char in trie
        self.stream.appendleft(letter)
        node = self.trie
        # print("self.trie->", self.trie)
        for char in self.stream:   # Time: O(M)
            # print("char->", char)
            if "$" in node:
                return True
            if char not in node:
                return False
            node = node[char]
        return "$" in node
                

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
