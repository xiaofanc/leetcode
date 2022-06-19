"""
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.

"""

class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ""
        visited = set()
        for char in s:
            if (char.isupper() and char.lower() in visited) or (char.islower() and char.upper() in visited):
                if res == "" or char.upper() > res.upper():
                    res = char.upper()
            else:
                visited.add(char)
                
        return res
                