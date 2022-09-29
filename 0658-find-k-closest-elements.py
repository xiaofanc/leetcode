"""
find k element closest to target x
"""

class Solution:
	# Time: O(nlogn+klogk)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sorted_arr = sorted(arr, key = lambda num: abs(x-num))
        res = []
        for i in range(k):
            res.append(sorted_arr[i])
        return sorted(res)

    # Time: O(logn+k)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search to find the cloest num, then use two pointers
        def binarySearch(l, r):
            while l <= r:
                m = l + (r-l)//2
                if arr[m] == x:
                    return m
                elif arr[m] > x:
                    r = m - 1
                else:
                    l = m + 1
            return r
        
        l = binarySearch(0, len(arr)-1)  # -1
        r = l + 1                        # 0
        
        # l, r 都取不到!!
        while r - l - 1 < k:
            if l == -1:  # edge case: when there is no more nums in the left
                r += 1
                continue
            if r == len(arr):  # edge case: when there is no more nums in the right
                l -= 1
                continue
            # if r is closer
            if abs(arr[l]-x) > abs(arr[r]-x):
            # move right pointer to +1
                r += 1
            else:
            # move left pointer to -1 when abs(arr[l]-x) <= abs(arr[r]-x)
                l -= 1
        return arr[l+1: r]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search find the closest element <= x
        def binarySearch(l, r):
            while l <= r:
                m = l + (r-l)//2
                if arr[m] == x:
                    return m
                elif arr[m] < x:
                    l = m+1
                else:
                    r = m-1
            return r
        i = binarySearch(0, len(arr)-1)
        j = i+1
        while (i >= 0 or j <= len(arr)-1) and k > 0:
            if i == -1:
                j += 1
            elif j == len(arr):
                i -= 1
            elif i >= 0 and j <= len(arr)-1:
                if abs(arr[i]-x) <= abs(arr[j]-x):
                    i -= 1
                else:
                    j += 1
            k -= 1
        return arr[i+1:j]

if __name__ == '__main__':
	s = Solution()
	print(s.findClosestElements([1,2,3,4,5], 4, -1)) # [1,2,3,4]
    print(s.findClosestElements([1,2,3,4,5], 4, 3))  # [1,2,3,4]


