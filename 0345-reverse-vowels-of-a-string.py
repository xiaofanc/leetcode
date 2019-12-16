class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = []
        vowels = [c for c in s if c in "aeiouAEIOU"]
        for c in s:
            if c in "aeiouAEIOU":
                ans.append(vowels.pop())
            else:
                ans.append(c)
        return "".join(ans)
                
if __name__ == '__main__':
	s = Solution()
	print(s.reverseVowels("leetcode") == "leotcede")