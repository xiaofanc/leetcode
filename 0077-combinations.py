"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""
class Solution:
    # Time: O(k*(n!/(n-k)!k!))
    # Space: O(k) for recursion stack
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:])
            # 剪枝, last start index 至少从3开始
            last = n - (k-len(comb)) + 1 
            for i in range(first, last+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        
        output = []
        backtrack()
        return output

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]