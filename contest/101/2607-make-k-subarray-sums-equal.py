"""
You are given a 0-indexed integer array arr and an integer k. The array arr is circular. In other words, the first element of the array is the next element of the last element, and the last element of the array is the previous element of the first element.

You can do the following operation any number of times:

Pick any element from arr and increase or decrease it by 1.
Return the minimum number of operations such that the sum of each subarray of length k is equal.

Input: arr = [1,4,1,3], k = 2
Output: 1
Explanation: we can do one operation on index 1 to make its value equal to 3.
The array after the operation is [1,3,1,3]
- Subarray starts at index 0 is [1, 3], and its sum is 4 
- Subarray starts at index 1 is [3, 1], and its sum is 4 
- Subarray starts at index 2 is [1, 3], and its sum is 4 
- Subarray starts at index 3 is [3, 1], and its sum is 4 

Input: arr = [2,5,5,7], k = 3
Output: 5
Explanation: we can do three operations on index 0 to make its value equal to 5 and two operations on index 3 to make its value equal to 5.
The array after the operations is [5,5,5,5]
- Subarray starts at index 0 is [5, 5, 5], and its sum is 15
- Subarray starts at index 1 is [5, 5, 5], and its sum is 15
- Subarray starts at index 2 is [5, 5, 5], and its sum is 15
- Subarray starts at index 3 is [5, 5, 5], and its sum is 15 

Consider array 
[x, y, z, a, b, c]
Let k be 3. 
[x, y, z, a, b, c]
 |     |         - Let this Sum be A (x + y + z)
Now slide window
[x, y, z, a, b, c]
    |     |      - Let this Sum be B (A - x + a)
Here Sum of this subarray B can be equal to A only if a is equal to x. 

Therefore, we have following rules:
arr[i] == arr[i + k]
arr[i] == arr[i + 2 * k]
and so on.

So we need to find element in the same position of each cycle and make them equal.
elements in cycle 0: [2,7,5,5], median is 5 after sorting. all elements are picked, no need to continue

why median?
https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm/113336#113336
Recall that |𝑥−𝑠𝑖| is the distance between 𝑥 and 𝑠𝑖, so we are trying to minimize the sum of the distances.
One should notice that d|𝑥|/d𝑥 = sign(𝑥)(Being more rigorous would say it is a Sub Gradient of the non smooth 𝐿1 Norm function).
Hence, deriving the sum above yields ∑sign(𝑠𝑖−𝑥). This equals to zero only when the number of positive items equals the number of negative which happens when 𝑥 = median{𝑠1,𝑠2,⋯,𝑠𝑁}
.
"""
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # for each position i, we collect all elements in the k-cycle. Then, we determine the median and perform operations to make all elements equal to that median.
        res = 0
        # split numbers into k groups, do not visit an element twice
        for i in range(k):
            group = []
            visited = set()
            j = i
            while arr[j] != 0:
                group.append(arr[j])
                arr[j] = 0
                # element in the next group
                j = (j + k) % len(arr)
            # print("group ", group)
            # calculate the median for each group and make all elements = median
            group.sort()
            for n in group:
                res += abs(n - group[len(group)//2])
        return res

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        gcd = math.gcd(n, k)
        ans = 0
        for i in range(gcd):
            tmp = sorted([arr[j] for j in range(i, n, gcd)])
            median = tmp[len(tmp) // 2]
            ans += sum(abs(num - median) for num in tmp)
        return ans
        

