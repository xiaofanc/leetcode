class Solution:
    # Time: O(n)
    def reverseWords(self, s: str) -> str:
        chars = s.split(" ")
        chars = [char for char in chars if char != ""]
        res = ""
        for char in chars[::-1]:
            res += char + " "
        return res[:-1]

        # return " ".join(reversed(s.split()))
            
s = Solution()
print(s.reverseWords("the sky is     blue")) # "blue is sky the"