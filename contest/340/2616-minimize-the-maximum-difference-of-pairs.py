"""
Intuition:
To minimize the maximum difference amongst all the pairs, we need to find a maximum difference 
that satisfies the given condition of having p pairs of indices of nums. 
Since we want to minimize the maximum difference, we can use binary search to find the smallest 
maximum difference that satisfies the given condition.

Approach:
Sort the array as the difference between 2 adjacent elements in sorted array is least.
Binary search over maximum difference of possible pairs A[-1]-A[0].
count no. of possible pairs for the mid value skipping the pair if difference is more than mid.

note that the indices can be picked in atmost 1 pairs, so after you pick an index in a pair, do not pick it in another pair.
    - if A[i]-A[i-1] <= mid, count += 1, next check A[i+2]-A[i+1]
    - else check A[i+1] - A[i] <= mid, count += 1, next check A[i+3]-A[i+2]

if no. of possible pairs>=p store mid in hi as the last possible answer.
this step also decreases the range to search as the next answer if possible will be < hi.

more explanation:
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/solutions/3396031/explained-simple-and-clear-python3-code/

First, we sort the input list of integers. We define the minimum and maximum possible values 
for the maximum difference. The minimum value is 0 since the difference between any two elements 
is at least 0. The maximum value is the difference between the largest and smallest elements 
in the list since that is the maximum difference possible.

We perform binary search for the smallest maximum difference that satisfies the given condition.
In each iteration, we calculate the mid-point of the possible range of maximum differences. 
We then count the number of pairs of adjacent integers with a difference less than or equal to 
the mid-point maximum difference. If the number of such pairs is greater than or equal to p, 
we decrease the maximum possible value of the maximum difference. Otherwise, we increase the 
minimum possible value of the maximum difference.

We continue this process until the minimum and maximum values converge to the same value, 
which is the smallest maximum difference that satisfies the given condition.
"""

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Time: nlogn + nlog(max_diff - min_diff)
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            # possible max difference
            mid = left + (right - left) // 2
            # count the pairs with diff <= mid
            # = count total possible pairs if mid is the max value
            i = 1
            count = 0 
            while i < n:
                if nums[i] - nums[i-1] <= mid:
                    count += 1
                    i += 1
                i += 1
            if count >= p: # max value is too large
                right = mid
            else:
                left = mid + 1
        return left

        


