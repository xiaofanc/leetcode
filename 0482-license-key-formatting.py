class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-","").upper()[::-1]
        return "-".join(S[i:i+K] for i in range(0,len(S),K))[::-1]

if __name__ == '__main__':
	s = Solution()
	print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))