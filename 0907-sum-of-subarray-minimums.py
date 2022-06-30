"""
monotonic(non-decreasing) stack:
https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)
res[i] store the minsum for subarrays ending with arr[i]    
create non-decreasing stack to find the previous arr[j] that <= arr[i]
reuse the res[j] for res[i] since res[i] = res[j] + arr[i] * (i-j)
why?
since arr[i] > arr[j], add arr[j+1:i+1] to subarrays which end with arr[j] does not change the min sum of subarrays
add all extra subarrays for arr[j+1:i+1], which all has arr[i] as the min since arr[j] is the first number that <= arr[i]

A = [3,1,2,5,4]
3: [3]
1: [3,1], [1]
2: [3,1,2], [1,2], [2]
5: [3,1,2,5], [1,2,5], [2,5], [5]
4: [3,1,2,5,4], [1,2,5,4], [2,5,4], [5,4], [4]

We can denote by result[i] the sum of min values of those subarrays (ending with i-th element). Here are they:
3: 3
1: 1 + 1
2: 1 + 1 + 2
5: 1 + 1 + 2 + 5
4: 1 + 1 + 2 + 4 + 4
result = [3,2,4,9,12]

If we find previous value A[j] <= A[i] (j<i) then result[i] = result[j] + A[i]*(i-j)
for i == 4:
minvalue for [3,1,2,5,4], [1,2,5,4], [2,5,4] is the same as
minvalue for [3,1,2], [1,2], [2]

And the minvalue for extra subarrays [5,4], [4] are all = 4.
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # res[i] store the minsum for subarrays ending with arr[i]
        # add 0 in the beginning to avoid empty stack
        arr = [float("-inf")] + arr
        res = [0] * len(arr)
        # non-decreasing stack to find the first previous arr[j] that <= arr[i]
        stack = [0]
        for i in range(1, len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            # arr[j] is the first number <= arr[i]
            j = stack[-1]
            # reuse the res[j] for res[i] since res[i] = res[j] + arr[i] * (i-j)
            res[i] = res[j] + arr[i] * (i-j)
            stack.append(i)
        return sum(res) % (10 ** 9 + 7)

if __name__ == '__main__':
	s = Solution()
	print(s.sumSubarrayMins([3,1,2,5,4])) # res = [3,2,4,9,12]


