class Solution:
    # Time: O(NlogN+N)
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        cnt = 0
        # sort in ascending order of attack and descending order of defense
        # why ascending order of attack?
        # Then we can loop from right to left and only need to keep track of the max defense
        # why descending order of defense?
        # [(4,3),(4,2),(5,1)]
        # we do not want [(4,2),(4,3),(5,1)] since max D = 3 when reaching (4,2), then (4,2) will be miscalculated as a weak character
        properties.sort(key=lambda x: (x[0], -x[1]))
        D = 0
        # keep track of the max defense for attack+1
        for i in range(len(properties)-1,-1,-1):
            if properties[i][1] < D:
                cnt += 1
            else:
                D = properties[i][1]
        return cnt
                    
    # bucket sort: index as attack, value as defense for attack >= i
    # Time: O(N+K)
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # the pair (a, b) will be weak if the maximum defense value stored for value a + 1 is greater than b
        cnt = 0
        maxAttack = max([p[0] for p in properties])
        arr = [0]*((maxAttack+2))
        # get the max defense for each attack i
        # same as bucket sort
        for a, d in properties:
            arr[a] = max(arr[a], d)
        
        # arr[i] = max defense for attack >= i, accumulative max defense
        D = 0
        for a in range(len(arr)-1,-1,-1):
            D = max(D, arr[a])
            arr[a] = D
            
        # for each pair, compare with max defense for attack+1
        for a, d in properties:
            if d < arr[a+1]:
                cnt += 1
        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfWeakCharacters([[4,2],[4,3],[5,1]])) # 0




