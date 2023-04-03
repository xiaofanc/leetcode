class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        n = len(potions)

        def bs(potions, s):
            l, r = 0, n-1
            while l <= r:
                m = l + (r-l) // 2
                if s * potions[m] >= success:
                    r = m-1
                else:
                    l = m+1
            return l

        for i, s in enumerate(spells):
            total = 0
            # binary search to find the first p which make s*p >= success
            # p = [1,2,3,4,5]
            idx = bs(potions, s)
            total += n-idx
            # for j, p in enumerate(potions):
            #     if s * p >= success:
            #         total += 1
            #     else:
            #         break
            res.append(total)
        return res

    # two pointers
    # if the spells and potions arrays are sorted in increasing order, and we know where 
    # the minPotion for the ith spell is present in the potions array, then the minPotion 
    # for the (i+1)th spell will be present at the same or smaller index as for the ith spell
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:    
        sortedspells = [(s, i) for i, s in enumerate(spells)]
        sortedspells.sort()
        potions.sort()
        n = len(potions)

        res = [0] * len(spells)
        # for each spell, find the minimum potions p * s >= success
        # for larger spell, the minimum potions required will be less than previous p
        minp = n-1
        for s, i in sortedspells:
            while minp >= 0 and s * potions[minp] >= success:
                minp -= 1
            res[i] = n - (minp + 1)
        return res





