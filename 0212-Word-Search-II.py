"""
input: [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
["oath","digs","dog","dogs"]
build trie: {'o': {'a': {'t': {'h': {'$': 'oath'}}}}, 'd': {'i': {'g': {'s': {'$': 'digs'}}}, 'o': {'g': {'$': 'dog', 's': {'$': 'dogs'}}}}}

Trie: prefix tree
check all the words that we can create starting from every position in the board

Time: O(MxNx(4x3^L)) == O(MxNx(4^L))
If we apply the optimization trick to gradually remove the nodes in Trie, we could greatly improve the time complexity, since the cost of backtracking would reduced to zero once we match all the words in the dictionary, i.e. the Trie becomes empty.

Space: O(N)
The main space consumed by the algorithm is the Trie data structure we build. 
"""
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        for (dx, dy) in [(1,0), (0,1), (-1,0), (0,-1)]:
            self.dfs(board, node, i+dx, j+dy, path+tmp, res)
        board[i][j] = tmp

    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_key = "$"
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # if letter not in the dictionary, return default {}
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[word_key] = word
        # print(trie)
        row, col = len(board), len(board[0])
        res = []
        
        def backtracking(row, col, parent):
            tmp = board[row][col]
            # get the children dictionary
            node = parent[tmp] 
            # check if we find a match of the word
            # The pop() method removes and returns an element from a dictionary having the given key
            word_match = node.pop(word_key, False)
            if word_match:
                res.append(word_match)
            # mark the node as visited before exploration
            board[row][col] = "#"
            for (dx, dy) in [(1,0), (-1,0), (0,1), (0,-1)]:
                newRow, newCol = row+dx, col+dy
                if newRow < 0 or newRow >= len(board) or newCol < 0 or newCol >= len(board[0]):
                    continue 
                # if the neighbor is not in the children dictionary then continue
                if board[newRow][newCol] not in node:
                    continue
                # backtrack along the nodes in Trie
                backtracking(newRow, newCol, node)
            board[row][col] = tmp

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not node:
                parent.pop(tmp)

        for i in range(row):
            for j in range(col):
                # check if the starting cell letter is in the dictionary
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return res
        
            
if __name__ == '__main__':
    s = Solution()
    print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
            