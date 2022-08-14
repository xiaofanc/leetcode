

class Solution:
	# TLE
    def findLadders(self, start: str, end: str, wordList: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "#" + word[i+1:]
                dct[pattern].append(word)
        
        queue = deque([(start, [start])])
        res = []
        depth = 0
        seen = set([start])
        while queue:
            level = len(queue)
            level_visited = set()
            # check the path with same length
            for _ in range(level): 
                word, path = queue.popleft()
                # print("word, d, path", word, d, path)
                # print("queue =====>", queue)
                # print("seen->", seen)
                if word == end:
                    res.append(path)
                    continue  # stop extending the path
                for i in range(len(word)):
                    pattern = word[:i] + "#" + word[i+1:]
                    for j, nei in enumerate(dct[pattern]):
                        if nei not in seen:
                        	# path[:]+[nei] != path.append(nei)
                        	# path.append(nei) will append all the nei to the path - not correct
                        	# path[:]+[nei] work like backtrack
                            queue.append((nei, path[:]+[nei]))
                            level_visited.add(nei)
            # only update the set when each nei is visited
            seen.update(level_visited)
        return res
                    
            

