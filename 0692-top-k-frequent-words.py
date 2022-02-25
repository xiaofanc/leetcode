class Solution:
    # Time: O(nlogn)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        res = sorted(counter, key=lambda x: (-counter[x], x)) 
        return res[:k]

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(["i","love","leetcode","i","love","coding"], 2)) # ["i","love"]
