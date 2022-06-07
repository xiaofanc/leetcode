"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions

The problem can also be viewed as finding the kth smallest element from m sorted arrays.

      2   4   6
   +------------
 1 |  3   5   7
 7 |  9  11  13
11 | 13  15  17


It starts off only with the very first pair at the top-left corner of the matrix, and expands from there as needed. Whenever a pair is chosen into the output result, the next pair in the row gets added to the priority queue of current options. Also, if the chosen pair is the first one in its row, then the first pair in the next row is added to the queue.

The problem can also be viewed as finding the kth smallest element from m sorted arrays. The 'bubbling' down process in your solution 5 can also be seen as keeping track of the smallest element in each array. 

The priority queue will take care of putting the pair with minimum sum to the first.
"""

class Solution:
	# TLE
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, product(nums1, nums2), key=sum)

    def kSmallestPairs(self, nums1, nums2, k):
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            # Why is it always push(i, j+1) here? Why couldn't it be push(i+1, j)? Why is the next candidate to its right, not below it?
            # This part allows the top row to be covered
            push(i, j + 1)
            # If the chosen pair is the first one in its row, then the first pair in the next row is added to the queue. Why?
            # This part allows going down from existing spots
            if j == 0:
                push(i + 1, 0)
        return pairs            

if __name__ == '__main__':
	s = Solution()
	print(s.kSmallestPairs([1,7,11], [2,4,6], 3))
