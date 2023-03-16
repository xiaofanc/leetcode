class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        p = 0
        prev = 0
        while p < len(arr):
            if arr[p] != prev+1:
                for j in range(prev+1, arr[p]):
                    k -= 1
                    if k == 0:
                        return j
            prev = arr[p]
            p += 1
        return prev+k            

    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k <= arr[0]-1:
            return k
        k -= arr[0]-1

        for i in range(len(arr)-1):
            cur_missing = arr[i+1]-arr[i]-1
            if k <= cur_missing:
                return arr[i]+k
            else:
                k -= cur_missing
        return arr[-1]+k

    # binary search:
    # missing numbers before current position: arr[idx]-idx-1
    # If the number of positive integers which are missing before arr[pivot] is less than k: 
    # continue to search on the right side of the array. Otherwise, continue to search on the left side.
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right - left) // 2
            # search right
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # left = right+1, and the kth missing number is between arr[right] and arr[left]
        # the number of missing numbers before right is arr[right]-right-1
        # the kth missing number = arr[right]+k-(arr[right]-right-1)
        return k + right + 1






