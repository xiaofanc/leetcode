"""
return the intersection of two interval lists
Each list of intervals is pairwise disjoint and in sorted order
"""
class Solution:
    def intervalIntersection(self, f: List[List[int]], g: List[List[int]]) -> List[List[int]]:
        # two pointers i, j
        i, j = 0, 0
        res = []
        while i < len(f) and j < len(g):
            s1, e1 = f[i][0], f[i][1]
            s2, e2 = g[j][0], g[j][1]
            # if f[i] and s[j] has intersection:
            if not (e1 < s2 or s1 > e2):
            # get the intersection [max(start1, start2), min(end1, end2)]
                res.append((max(s1, s2), min(e1, e2)))
            # move the pointer that points to the smaller end
            # If A[0] has the smallest endpoint, it can only intersect B[0]. 
            # After, we can discard A[0] since it cannot intersect anything else in B since B is disjoint.
            if e1 > e2:
                j += 1
            elif e1 < e2:
                i += 1
            else: # same end, each list is pairwise disjoint
                i += 1
                j += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])) # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
