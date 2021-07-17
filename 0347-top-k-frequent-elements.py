class Solution:
    # Time: O(n+k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dct = collections.Counter(nums)
        #print(sorted(nums_dct.items(), key=lambda item: -item[1]))
        res = [key for key, val in sorted(nums_dct.items(), key=lambda item: -item[1])]
        return res[:k]

    # Time: O(nlogk)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3]), 2)