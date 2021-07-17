class Solution:
    # time: O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # pick a random pivot
        # using partition algorithm to separate the nums
        # find kth largest == find n-k th smallest
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
            
if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4]), 2)







    