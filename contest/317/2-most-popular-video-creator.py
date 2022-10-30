
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        cids = defaultdict(list)
        ctotal = defaultdict(int)
        for c, i, v in zip(creators, ids, views):
            cids[c].append((v, i))
            ctotal[c] = ctotal.get(c, 0) + v
        maxc, maxv = [], 0
        for k, v in ctotal.items():
            if v > maxv:
                maxv = v
                maxc = [k]
            elif v == maxv:
                maxc.append(k)
        res = []
        for c in maxc:
            sortedid = sorted(cids[c], key=lambda x: (-x[0], x[1]))
            res.append((c, sortedid[0][1]))
        return res
            
            