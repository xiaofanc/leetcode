"""
Return a list of lists of the suggested products after each character of searchWord is typed
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefixMap = defaultdict(list)
        for i in range(1, len(searchWord)+1):
            for p in products:
                if searchWord[:i] == p[:i]:
                    prefixMap[p[:i]].append(p)
        res = []
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]
            match = sorted(prefixMap[prefix])[:3]
            res.append(match)
        return res


# use Trie
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
            node.words.sort()
            while len(node.words) > 3:
                node.words.pop()
    
    def search(self, word):
        res = []
        node = self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            res.append(node.words[:])
        l_remain = len(word) - len(res)
        for _ in range(l_remain):
            res.append([])
        return res

class Solution:
    # Time: O(mlogn) + O(logn)
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for prod in products: 
            trie.insert(prod)
        return trie.search(searchWord)

# binary search
class Solution:
    # Time: O(nlogm)
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        # binary search for every prefix
        l, r = 0, len(products)-1
        res = []
        # print("products", products)
        for index, char in enumerate(searchWord):
            # check the left boundary
            while l <= r and (len(products[l]) <= index or products[l][index] != char):
                l += 1
            while l <= r and (len(products[r]) <= index or products[r][index] != char):
                r -= 1
            res.append(products[l:min(l+3, r+1)])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.suggestedProducts(["havana"], "tatiana")) # [[],[],[],[],[],[],[]]


