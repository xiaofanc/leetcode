# There are two sorted arrays nums1 and nums2 of size m and n respectively. Find
# the median of the two sorted arrays. The overall run time complexity should be
# O(log (m+n)).
# 2 pointers

class Solution: 
    # time: O(m+n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        # when one pointer reaches the end
        if i == len(nums1): nums.extend(nums2[j:])
        if j == len(nums2): nums.extend(nums1[i:])
        return (nums[l//2-1] + nums[l//2])/2 if l % 2 == 0 else nums[l//2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1+len2) % 2 == 1:
            middle = (len1+len2) // 2
            return self.get_kth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, middle)
        else:
            middle1 = self.get_kth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (len1+len2) // 2 - 1)
            middle2 = self.get_kth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (len1+len2) // 2)
            return (middle1+middle2) / 2
        
    def get_kth(self, nums1, start1, end1, nums2, start2, end2, k):
        if start1 > end1:
            # kth is not in nums1 and 
            # num before start1 is less than kth, nums1[start1] is larger than kth
            # if k = 3, start1 = 1
            # nums1里面1个数比kth小，nums[2]就是合并后第kth的数
            return nums2[k-start1] 
        if start2 > end2:
            return nums1[k-start2] 
        m1 = (start1 + end1) // 2
        m2 = (start2 + end2) // 2
        m1v, m2v = nums1[m1], nums2[m2]
        if (m1+m2) < k:
            if m1v > m2v:
                # k is not in the left half of nums2
                return self.get_kth(nums1, start1, end1, nums2, m2+1, end2, k)
            else:
                return self.get_kth(nums1, m1+1, end1, nums2, start2, end2, k)     
        else:
            if m1v > m2v:
                # k is not in the right half of nums1
                return self.get_kth(nums1, start1, m1-1, nums2, start2, end2, k)
            else:
                return self.get_kth(nums1, start1, end1, nums2, start2, m2-1, k)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search the shortest array
        # get half numbers from nums1 and nums2
        # half numbers: A[:m+1], B[:j+1]
        # compare A[m] vs B[j], A[m+1] vs B[j+1] to see if we should include more or less nums from A
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        # A is the shorter array
        l, r = 0, len(A)-1
        total = len(A)+len(B)
        half = (total)//2
        # we need to find the correct half number
        # l = 0, r = -1 is fine since it is possible we do not include any number from A
        # so we cannot use while l <= r here
        while True:  
            m = l + (r-l)//2  
            j = half-m-2     # why -2 here? since index starts from 0, we need half numbers
            leftA = A[m] if m >= 0 else float('-inf')
            rightA = A[m+1] if m < len(A)-1 else float('inf')
            leftB = B[j] if j >= 0 else float('-inf')
            rightB = B[j+1] if j < len(B)-1 else float('inf')
            
            # we found the correct half numbers
            if leftA <= rightB and leftB <= rightA:
                if total % 2: # odd total number
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                # maker A smaller
                r = m - 1
            else:
                l = m + 1

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3],[2]))



    