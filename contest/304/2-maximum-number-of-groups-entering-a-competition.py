"""
It's given that the grades are always positive. So, irrespective of the values present in the grades array once we sort them in increasing order, we can always pick them in buckets, like 1, 2, 3,.. till the last bunch. This will satisfy size[bucket+1] > size[bucket] and sumOfGrades[bucket+1] > sumOfGrades[bucket].

The example in the question confuses us,

Input: grades = [10,6,12,7,3,5]
Output: 3
Explanation: The following is a possible way to form 3 groups of students:

1st group has the students with grades = [12]. Sum of grades: 12. Student count: 1
2nd group has the students with grades = [6,7]. Sum of grades: 6 + 7 = 13. Student count: 2
3rd group has the students with grades = [10,3,5]. Sum of grades: 10 + 3 + 5 = 18. Student count: 3
It can be shown that it is not possible to form more than 3 groups.
The same can be seen as, [3], [5, 6], [7, 10, 12] -> 3 ways, which is always true in a generic case.

After sort: [3, 5, 6, 7, 10, 12]
Bucket 1 with 1 element : [3]
Bucket 2 with 2 elements : [5, 6]
Bucket 3 with 3 elements : [7, 10, 12]

Explanation
Sort all grades,
assign 1 student to the first group,
assign 2 student to the second group...
This can satify ith group < i+1th group for both size and sum.

So we need to find out the maximum result k that
1 + 2 + ... + k <= n

solution 2:
use binary search to solve 1 + 2 + ... + k <= n
k(k+1)/2 <= n
The maximum groups formed can be 446 because (446 *(446+1)) / 2 is approximately 10^5. (Check constraints for n)
"""

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # sort the grade therfore sumOfGrades[bucket+1] > sumOfGrades[bucket] automatically satisfied if we have size[bucket+1] > size[bucket]
        # if we cannot meet size[bucket+1] > size[bucket], we do not care about the sum
        # we just need to build up the triangle
        grades.sort()
        cnt = 0
        k = 0
        n = len(grades)
        while n >= k+1:
            k += 1
            n -= k
            cnt += 1
        return cnt

if __name__ == '__main__':
	s = Solution()
	print(s.maximumGroups([10,6,12,7,3,5])) # 3




