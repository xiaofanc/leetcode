class Solution:
    # time: Quick select - O(n)
    # Similar to Quick sort.
    # However, there is no need to deal with both parts since now one knows in which part to search for N - kth smallest element, and that reduces average time complexity to O(N)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # pick a random pivot
        # using partition algorithm to separate the nums
        # find kth largest == find n-k th smallest value
        # compare pivot index and n-k, pick up one side
        # using partition algorithm again until pivot index == n-k
        def partition(l, r, pivot_idx):
            pivot = nums[pivot_idx]
            # move pivot to the end
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            # split the nums
            i = l-1
            for j in range(l, r):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            # swap i+1 with pivot to make pivot in the middle
            nums[i+1], nums[r] = nums[r], nums[i+1]
            return i+1
        
        def select(left, right, k_smallest):
            if left == right:
                return nums[left]

            pivot_idx = random.randint(left, right)
            # sort the nums based on nums[pivot_idx]
            pivot_idx = partition(left, right, pivot_idx)
            
            if pivot_idx == k_smallest:
                return nums[pivot_idx]
            elif pivot_idx > k_smallest:
                # pick the left side
                return select(left, pivot_idx-1, k_smallest)
            else:
                # pick the right side
                return select(pivot_idx+1, right, k_smallest)
        
        return select(0, len(nums)-1, len(nums)-k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def select(l, r, ksmallest):
            # select the kth smallest 
            # base case:
            if l == r:
                return nums[l]
            # select a random index
            pivot = random.randint(l, r)
            # update the correct position of selected random value
            pivot = partition(l, r, pivot)
            if pivot == ksmallest:
                return nums[ksmallest]
            elif pivot > ksmallest:
                # search the left partition
                return select(l, pivot-1, ksmallest)
            else:
                # search the right partition
                return select(pivot+1, r, ksmallest)

        def partition(l, r, pivot):
            # sort the nums based on pivot value
            mid = nums[pivot]
            nums[l], nums[pivot] = nums[pivot], nums[l]
            s, e = l+1, r
            # while s < e is not correct for edge cases when mid is the largest or smallest
            while s <= e:
                while s <= e and nums[s] < mid:
                    s += 1
                while s <= e and nums[e] >= mid:
                    e -= 1
                # swap
                if s < e:
                    nums[s], nums[e] = nums[e], nums[s]
            # when s == e, e points to the last number < mid
            # s 可能会出界, e不会出界，最小为0
            nums[l], nums[e] = nums[e], nums[l]
            return e
        
        return select(0, len(nums)-1, len(nums)-k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        Pos = [0]*10**5
        Neg = [0]*10**5
        largest = float('-inf')
        Poscount = 0  # positive int

        for n in nums:
            if n >= 0:
                Pos[n] += 1
                Poscount += 1
            else:
                Neg[-n] += 1
            largest = max(largest, n)
            
        if Poscount >= k:
            # res is in the positive arr
            for i in range(largest, -1, -1):
                while Pos[i] > 0:
                    Pos[i] -= 1
                    k -= 1
                    if k == 0:
                        return i
        else:
            # res is in the negative arr
            k -= Poscount
            for i in range(10**5):
                while Neg[i] > 0:
                    Neg[i] -= 1
                    k -= 1
                    if k == 0:
                        return -i

if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4]), 2)








    