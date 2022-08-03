"""
Given an array nums, there is a sliding window of size k which is moving from the 
very left of the array to the very right. You can only see the k numbers in the 
window. Each time the sliding window moves right by one position. Return the max 
sliding window.

using double-ended queue 双端队列: O(n) the structure which pops from / pushes to 
either side with the same O(1) performance.

If the current number is larger than the number in the double-ended queue,
then pop the number in the double-ended queue, and append the current number. 
Else append the number to the double-ended queue 

The largest number is always in the beginning in the double-ended queue 

[1, 3, -1, -3, 5, 3, 6, 7]    k = 3
a. Process the first k elements separately to initiate the deque.
b. Iterate over the array. At each step :
    Clean the deque :
    Keep only the indexes of elements from the current sliding window.
    Remove indexes of all elements smaller than the current one, since they will not be the maximum ones.
    Append the current element to the deque.
c. Return the output array.

Append deque[0] to the output.
deque = [1], 3
deque = [3], -1
deque = [3, -1], -3         max = [3]
deque = [3, -1, -3], 5      max = [3, 3]
deque = [5], 3              max = [3, 3, 5]
deque = [5, 3], 6           max = [3, 3, 5, 5]
deque = [6], 7              max = [3, 3, 5, 5, 6]
deque = [7]                 max = [3, 3, 5, 5, 6, 7]
res = [3, 3, 5, 5, 6, 7] (always append the head of the deque)

单调队列:
主要思想是队列没有必要维护窗口里的所有元素，只需要维护有可能成为窗口里最大值的元素就可以了，同时保证队列里的元素数值是由大到小的。

"""
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # base cases
        n = len(nums)
        if n*k == 0:
            return 
        if k == 1:
            return nums
        
        def clean_deque(i):
            # remove left if the index is out of current window
            while deq and deq[0] <= i-k:
                deq.popleft()
            # pop the numbers in deq which is smaller than the current number
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        # initiate dequeue:
        deq = deque() # store index
        res = []
        # get the maximum from the first k numbers
        for i in range(k):
            clean_deque(i)
            deq.append(i)
        res.append(nums[deq[0]])
        # create output
        for j in range(k, n):
            clean_deque(j)
            deq.append(j)
            res.append(nums[deq[0]])
        return res

    # Time: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # queue stores the index of the max number in the sliding window
        q = deque() # store index
        res = []
        for i, n in enumerate(nums):
            # if the current number is larger than the number in the queue, then pop
            while q and n > nums[q[-1]]:
                q.pop()
            q.append(i) # [3,-1,-3]
            # check if the index of the max num is out of current window
            if q[0] == i-k:
                q.popleft()
            # when to get max num from queue
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    assert s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]







