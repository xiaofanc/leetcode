
class Solution:
    def partitionString(self, s: str) -> int:
        res = []
        def partition(i, s):
            if not s:
                return 0
            subs = ""
            unique = set()
            for j in range(i, len(s)):
                if s[j] not in unique:
                    subs += s[j]
                    unique.add(s[j])
                else:
                    res.append(subs[:])
                    subs = s[j]
                    unique = set(s[j])
            res.append(subs[:])
            
        partition(0, s)
        return len(res)
                    
    def partitionString(self, s: str) -> int:
        r = 0
        res = 1
        visited = set()
        while r < len(s):
            if s[r] in visited:
                res += 1
                visited = set()
            visited.add(s[r])
            r += 1
        return res


        