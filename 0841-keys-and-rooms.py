class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(i):
            visited.add(i)
            if len(visited) == len(rooms):
                return True
            for nei in rooms[i]:
                if nei not in visited:
                    if dfs(nei):
                        return True
            return False
        
        return dfs(0)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(i):
            if i not in visited:
                visited.add(i)
                if len(visited) == len(rooms):
                    return True
                for nei in rooms[i]:
                    if dfs(nei):
                        return True
            return False
        
        return dfs(0)

                