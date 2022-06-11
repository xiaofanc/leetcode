"""
does not pass ["a"," "," ","b"] 
"""

class Solution:
    # Time: O(n), Space: O(1)
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseword(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            
        reverseword(0, len(s)-1)
        
        left = 0
        for index, char in enumerate(s):
            if char == " ":
                reverseword(left, index-1)
                left = index+1
        reverseword(left, len(s)-1)
                    
if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"])) # ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]