"""
2399.
"""


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        visited = {}
        for i, char in enumerate(s):
            d = ord(char) - ord('a')
            if char in visited:
                if i-visited[char]-1 != distance[d]:
                    return False
            else:
                visited[char] = i
        return True
    
                
        