class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # BFS
        def findMutations(source, j):
            mutations = []
            copy = source[:]
            for g in ["A","C","G","T"]:
                if g != source[j]:
                    copy[j] = g
                    mutations.append("".join(copy))
                    copy = source[:]
            return mutations
            
        queue = deque()
        visited = set()
        queue.append(start)
        visited.add(start)
        step = 0
        bankSet = set(bank)
        
        while queue:
            size = len(queue)
            for i in range(size):
                gene = queue.popleft()
                if gene == end:
                    return step
                # add all possible neighbors from the bank
                genechar = [char for char in gene]
                for j in range(8):
                    for mutation in findMutations(genechar, j):
                        if mutation in bankSet and mutation not in visited:
                            queue.append(mutation)
                            visited.add(mutation)
            step += 1
        return -1
                        
                    
            