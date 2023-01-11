
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = ""
        i = 0
        idxmap = {}
        for idx, si in enumerate(indices):
            idxmap[si] = idx

        while i < len(s):
            if i in idxmap:
                old = sources[idxmap[i]]
                # if substring is found
                if s[i:i+len(old)] == old:
                    # replace
                    res += targets[idxmap[i]]
                    i += len(old)
                else:
                    res += s[i]
                    i += 1
            else:
                res += s[i]
                i += 1
        return res

    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # in-place s, sort indexes and do it from right to left
        size = len(s)
        idxmap = {}
        for idx, si in enumerate(indices):
            idxmap[si] = idx

        for i in range(size-1,-1,-1):
            if i in idxmap:
                old = sources[idxmap[i]]
                # if substring is found
                if s[i:i+len(old)] == old:
                    # replace
                    s = s[:i] + targets[idxmap[i]] + s[i+len(old):]
        return s

    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # in-place s, sort indexes and do it from right to left
        for i, so, t in sorted(zip(indices, sources, targets), reverse = True):
            s = s[:i] + t + s[i+len(so):] if s[i:i+len(so)] == so else s
        return s



        
