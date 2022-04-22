class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.addWord(word)
        # print("trie", trie)
        
        m, n = len(board), len(board[0])
        res = set()
        
        def backtrack(x, y, node, word):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == "#" or board[x][y] not in node.children:
                return
            tmp = board[x][y]
            word += tmp
            node = node.children[tmp]
            board[x][y] = "#"
            if node.isWord:
                res.add(word)
                # return
            for (dx, dy) in [(1,0), (0,1), (-1,0), (0,-1)]:
                backtrack(x+dx, y+dy, node, word)
            board[x][y] = tmp

            # if not node: # leaf
            	# parent.children.pop(tmp)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    backtrack(i, j, trie, "")
        return list(res)
                    
if __name__ == '__main__':
    s = Solution()
    print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
 

