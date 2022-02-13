class Solution:
    # Time: O(n)
    def minDeletions(self, s: str) -> int:
        counts = collections.Counter(s) # O(n)
        # print(counts)
        unique = set()
        ans = 0
        for key, value in counts.items():
            if value not in unique:
                unique.add(value)
            else:
                while value in unique and value > 0:
                    ans += 1
                    value -= 1
                unique.add(value)
        return ans

    def minDeletions(self, s: str) -> int:
        counts = collections.Counter(s)
        # print(counts)
        unique = set()
        ans = 0
        for key, value in counts.items():
            while value > 0 and value in unique:
                value -= 1
                ans += 1
            unique.add(value)
        return ans
        
if __name__ == '__main__':
    s = Solution()
    print(s.minDeletions("aaabbbcc"))  #2