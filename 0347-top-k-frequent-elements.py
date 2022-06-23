"""
我们要用小顶堆，因为要统计最大前k个元素，只有小顶堆每次将最小的元素弹出，最后小顶堆里积累的才是前k个最大元素。

Time for heap:
heappush/heappop: logn
heapify: O(n)
"""
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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums) # O(n)
        heap = []
        
        # build a heap of size k using n elements - O(nlogk)
        # height of the binary heap: logk
        # 先加进去再pop
        for key, value in count.items():
            heapq.heappush(heap, (value, key)) 
            if len(heap) > k: 
                heapq.heappop(heap) # pop the small values
        
        # convert the heap into array - O(klogk)
        res = [0] * k
        for i in range(k-1, -1, -1):
            res[i] = heapq.heappop(heap)[1] # get the key
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3]), 2)


