class Solution:
    # passed 60 cases
    # did not pass ["coswcmcgkc","cosgmccwkc","coswmccgkc"]
    # They should be in the same group. However, the first two already in different groups
    # Use graph to connect them!
    def numSimilarGroups(self, strs: List[str]) -> int:
        groups = [set([strs[0]])]
        for s in strs[1:]:
            # print("s ", s)
            for g in groups:
                found = False
                for word in g:
                    # print("word ", word)
                    dct = {}
                    swap = 0
                    for i, c in enumerate(s):
                        # print("i, c, ", i, c)
                        if c != word[i]:
                            if c in dct and dct[c] == word[i]:
                                swap += 1
                            elif word[i] not in dct:
                                dct[word[i]] = c
                                swap += 1
                                # print("     dct ", dct)
                            if swap > 2:
                                break
                            # print("     swap ", swap)
                    if swap == 0 or swap == 2:
                        g.add(s)
                        found = True
                        break
                if found:
                    break
            if not found:
                groups.append(set([s]))
        return len(groups)


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        adj = defaultdict(list)
        def isSimilar(w1, w2):
            # w1 and w2 is anagram
            diff = 0
            for i, c in enumerate(w1):
                if c != w2[i]:
                    diff += 1
            return diff == 0 or diff == 2

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if isSimilar(strs[i], strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        groups = 0
        visited = set()
        for i in range(len(strs)):
            if i not in visited:
                dfs(i)
                groups += 1
        return groups


