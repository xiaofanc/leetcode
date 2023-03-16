class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indexes = defaultdict(list)
        for i, num in enumerate(arr):
            indexes[num].append(i)
        
        steps = 0
        visited = set()
        visited.add(0)
        cur = [0]

        while cur:
            nex = []

            for j in cur:
                if j == len(arr)-1:
                    return steps

                for nei in indexes[arr[j]]:
                    if nei not in visited:
                        visited.add(nei)
                        nex.append(nei)
                
                indexes[arr[j]].clear()

                for child in [j-1, j+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)
            steps += 1
            cur = nex
        
        return -1

            
