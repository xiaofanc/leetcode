"""
2491.
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
"""
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        teams = len(skill) / 2
        if sum(skill) / teams != sum(skill) // teams:
            return -1
        target = sum(skill) / teams
        
        visited = dict()
        p = 0
        for s in skill:
            if target - s not in visited:
                visited[s] = visited.get(s, 0) + 1
            else:
                visited[target-s] -= 1
                if visited[target-s] == 0:
                    del visited[target-s]
                p += int(s*(target-s))
        if len(visited) != 0:
            return -1
        return p
                
        
        
        