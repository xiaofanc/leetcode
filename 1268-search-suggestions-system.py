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

