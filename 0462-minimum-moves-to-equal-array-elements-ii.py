"""
solution 1. brute force
In this approach, rather than choosing every possible k between the minimum and the maximum values in the array, we can simply consider k as every element of the array. 

solution 2. Find a point k such that the cumulative sum of distances between k and the rest of the points is minimum. This is a very common mathematical problem whose answer is known. The point k is the median of the given points. 

solution 3. if we observe properly, we'll find that if the array is sorted, we can do the same task without actually finding the median or the number k to which we need to settle at the end. 

We know, at the end, both these numbers should be equalized to k. For the number max, the number of moves required to do this is given by max−k. Similarly, for the number min, the number of moves is given by k - min. Thus, the total number of moves for both max and min is given by max - k + (k - min) = max - min, which is independent of the number k. Thus, we can continue now, with the next maximum and the next minimum number in the array, until the complete array is exhausted.

"""

class Solution:
	# brute force: time: O(n^2)
    def minMoves2(self, nums: List[int]) -> int:
        minv = float('inf')
        for n in nums:
            moves = 0
            # print("n: ", n)
            for m in nums:
                # print("m: ", m)
                moves += abs(m - n)
            # print("moves -->", moves)
            minv = min(moves, minv)
        return minv

    # Time: O(nlogn) - sort
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        moves = 0
        for n in nums:
            moves += abs(nums[len(nums)//2] - n)
        return moves

    # Time: O(nlogn) - sort
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l, r = 0, len(nums)-1
        ans = 0
        while l < r:
            ans += (nums[r] - nums[l])
            l += 1
            r -= 1
        return ans

if __name__ == '__main__':
	s = Solution()
	print(s.minMoves2([1,3,2])) # 2



