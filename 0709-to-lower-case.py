class Solution:
    def toLowerCase(self, S: str) -> str:
        return "".join(chr(ord(s) + 32) if 65 <= ord(s) <= 90 else s for s in S)
                
if __name__ == '__main__':
	s = Solution()
	print(s.toLowerCase("LOVELY"))