class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return B in A+A and len(A) == len(B)

if __name__ == '__main__':
	s = Solution()
	print(s.rotateString('abcde', 'cdeab'))
	print(s.rotateString('abcde', 'abced'))