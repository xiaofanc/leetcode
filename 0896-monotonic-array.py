from typing import List

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return sorted(A) == A or list(reversed(sorted(A))) == A

    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i] <= A[i+1] for i in range(len(A)-1)) or all(A[i] >= A[i+1] for i in range(len(A)-1))

if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic([1,2,2,3])) # true
    print(s.isMonotonic([6,5,4,4])) # true
    print(s.isMonotonic([1,3,2])) # false
    print(s.isMonotonic([1,2,4,5])) # true
    print(s.isMonotonic([1,1,1])) # true