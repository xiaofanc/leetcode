"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

explanation: sum of (len(connected component)-1)
"""

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]] -> 4
        def dfs(node):
            nonlocal moves
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    moves += 1
                    print("next_node, ", next_node, moves)
                    dfs(next_node)
        
        graph , moves , visited = defaultdict(list) , 0 , set()
        for i in range(len(stones)):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    # store index of the stone in the same row or column
                    graph[i].append(j)
                    graph[j].append(i)
        for node in range(len(stones)):
            if node not in visited:
                dfs(node)
        return moves

if __name__ == '__main__':
	s = Solution()
	print(s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])) # 5
	print(s.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])) # 3
	print(s.removeStones([[0,0]])) # 0
	print(s.removeStones([[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]))  # 4


