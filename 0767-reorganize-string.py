"""
if max frequency > (len(s)+1) // 2: return ""
else: reorganize the string based on count
"""

class Solution:
	# Time: O(nlogk), space: O(k)
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)
        maxc, maxl = 0, ""
        for k, v in count.items():
            if v > maxc:
                maxc = v
                maxl = k
        maxh = [(-v, k) for k, v in count.items()]
        heapq.heapify(maxh)  # O(n)
        res = []
        while maxh:
            v, k = heapq.heappop(maxh)
            if not res or res[-1] != k:
                res.append(k)
                if v+1 != 0:
                    heapq.heappush(maxh, (v+1, k))
            else:
                if not maxh:
                    return ""
                nextv, nextk = heapq.heappop(maxh)
                res.append(nextk)
                if nextv+1 != 0:
                    heapq.heappush(maxh, (nextv+1, nextk))
                heapq.heappush(maxh, (v, k))
        return ''.join(res)
                
                
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)
        maxc, maxl = 0, ""
        for k, v in count.items():
            if v > maxc:
                maxc = v
                maxl = k
        if maxc > (len(s)+1)//2:
            return ""
        # reorganize string odd/Even
        # place max freq letter first, then place rest of the letters in any order
        index = 0
        ans = ['']*len(s)
        while count[maxl] != 0:
            ans[index] = maxl
            index += 2
            count[maxl] -= 1
        
        for k, v in count.items():
            while v > 0:
                if index >= len(s):
                    index = 1
                ans[index] = k
                index += 2
                v -= 1
        return ''.join(ans)
    
                
                
            