class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        scounter, gcounter = {}, {}
        bull, cow = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                # add bull
                bull += 1              
            else:
                # increment both counter
                if s in scounter:
                    scounter[s] += 1
                else:
                    scounter[s] = 1
                if g in gcounter:
                    gcounter[g] += 1
                else:
                    gcounter[g] = 1
        # find common keys
        for key in scounter.keys() & gcounter.keys():
        # accumulate min count
            cow += min(scounter[key], gcounter[key])
        return "%sA%sB" %(bull, cow)

    def getHint(self, secret: str, guess: str) -> str:
        scount, gcount = [0]*10, [0]*10
        bull, cow = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                scount[int(s)] += 1
                gcount[int(g)] += 1
        for i, j in zip(scount, gcount):
            cow += min(i, j)
        return "%sA%sB" %(bull, cow)

if __name__ == '__main__':
    s = Solution()
    print(s.getHint("1807", "7810"))
