class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # l: (-(leftToRight + rightToLeft), -i), waiting on the left side, sort by efficiency
        # r: (-(leftToRight + rightToLeft), -i), waiting on the right side, sort by efficiency
        # ll: (time, i), on what time can move to l from new warehouse
        # rr: (time, i), on what time can move to r from old warehouse
        #  t defines the time of the last crossing

        ll, l, r, rr = [],[],[],[]
        t = 0

        for i,(l2r, po, r2l, pn) in enumerate(time):
            heappush(l, (-l2r-r2l, -i))
        
        while n:
            while ll and ll[0][0] <= t:
                # ll[0][1] is ready to cross
                _, i = heapq.heappop(ll)
                heapq.heappush(l, (-(time[i][0]+time[i][2]), -i))
            while rr and rr[0][0] <= t:
                # rr[0][1] is ready to cross
                _, i = heapq.heappop(rr)
                heapq.heappush(r, (-(time[i][0]+time[i][2]), -i))
            if r:
                # crossing
                _, i = heapq.heappop(r)
                t += time[-i][2]
                # Precompute the time when this worker can cross on the other side
                heapq.heappush(ll, (t+time[-i][3], -i))
                n -= 1
            elif l and n > len(r) + len(rr):
                # crossing
                _, i = heapq.heappop(l)
                t += time[-i][0]
                # Precompute the time when this worker can cross on the other side
                heapq.heappush(rr, (t+time[-i][1], -i))
            else:
                # update t to check which side will have people waiting first
                x = ll[0][0] if ll and n > len(r) + len(rr) else float('inf')
                y = rr[0][0] if rr else float('inf')
                t = min(x, y)
        return t
        
       