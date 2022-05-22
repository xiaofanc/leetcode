class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        scounter = collections.Counter(s)
        lcounter = collections.Counter(letter)
        res = 0
        for key, value in lcounter.items():
            res += scounter[key]
        return int(res / len(s) * 100)

if __name__ == '__main__':
    s = Solution()
    print(s.percentageLetter("foobar", "o")) # 33