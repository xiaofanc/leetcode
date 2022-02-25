class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrack(s, seen)
        
    def backtrack(self, s, seen):
        ans = 0
        if not s:
            return 0
        for i in range(1, len(s)+1):
            char = s[:i]
            if char not in seen:
                seen.add(char)
                ans = max(ans, 1 + self.backtrack(s[i:], seen))
                seen.remove(char)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxUniqueSplit("ababccc")) # 5