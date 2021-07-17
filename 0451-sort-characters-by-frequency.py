class Solution:
    # Time: O(nlogn)
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        new = ""
        for k, v in sorted(count.items(), key = lambda item: -item[1]):
        # for k, v in count.most_common(): # sort by the value
            new += k*v
        return new

if __name__ == '__main__':
    s = Solution()
    print(s.frequencySort("tree")) # "eetr"